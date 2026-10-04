from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.organizations_models import OrganisationModel
from app.models.organisation_members_model import OrgMemberModel
from app.models.user_models import UserModel
from app.schemas.organisation_schemas import OrganisationReq, OrganisationMemberReq


class OrganisationService:

    def __check_org_(org_id: str, db: Session):
        is_org = (
            db.query(OrganisationModel).filter(OrganisationModel.id == org_id).first()
        )

        if not is_org:
            raise HTTPException(status_code=404, detail=f"Org. not found with {org_id}")

        if not is_org.is_active:
            raise HTTPException(status_code=403, detail="Org. is not active")

        return is_org

    @staticmethod
    def get_all_org(db: Session):
        all_org = db.query(OrganisationModel).all()
        return all_org

    @staticmethod
    def create_org(data: OrganisationReq, db: Session):
        new_org = OrganisationModel(**data.model_dump())
        db.add(new_org)
        db.commit()
        db.refresh(new_org)
        new_org.members = []
        return new_org

    @staticmethod
    def add_user_to_org(data: OrganisationMemberReq, db: Session):
        OrganisationService.__check_org_(data.org_id, db)

        check_user = db.query(UserModel).filter(data.user_id == UserModel.id).first()
        if not check_user:
            raise HTTPException(
                status_code=404, detail=f"User not found with {data.user_id}"
            )

        check_already_added_user = db.query(OrgMemberModel).filter(OrgMemberModel.user_id == data.user_id).first()

        if check_already_added_user:
            raise HTTPException(status_code=400, detail=f"User already added with {data.user_id}")

        if not check_user.is_active:
            raise HTTPException(status_code=403, detail=f"User not active")

        new_org_mem = OrgMemberModel(**data.model_dump())
        db.add(new_org_mem)
        db.commit()
        db.refresh(new_org_mem)
        return new_org_mem

    @staticmethod
    def get_organisation(org_id: str, db: Session):
        org = OrganisationService.__check_org_(org_id, db)

        get_all_members = (
            db.query(OrgMemberModel).filter(OrgMemberModel.org_id == org_id).all()
        )

        org.members = get_all_members

        return org

    @staticmethod
    def org_members(org_id: str, db: Session):
        OrganisationService.__check_org_(org_id, db)
        get_all_members = (
            db.query(OrgMemberModel).filter(OrgMemberModel.org_id == org_id).all()
        )

        return get_all_members
