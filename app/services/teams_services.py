from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.organizations_models import OrganisationModel
from app.models.teams_models import TeamsModels, TeamMembersModel
from app.models.user_models import UserModel

from app.schemas.teams_schemas import TeamMemberReq, TeamsReq, TeamDeleteMember


class TeamService:

    def _check_org_(org_id: str, db: Session):
        check_org = (
            db.query(OrganisationModel).filter(OrganisationModel.id == org_id).first()
        )
        if not check_org:
            raise HTTPException(status_code=404, detail=f"Org not found with {org_id}")
        if not check_org.is_active:
            raise HTTPException(status_code=403, detail=f"Org is not active")
        return check_org

    def _check_user_(user_id, db: Session):
        check_user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not check_user:
            raise HTTPException(
                status_code=404, detail=f"User not found with {user_id}"
            )
        if not check_user.is_active:
            raise HTTPException(status_code=403, detail=f"User is not active")
        return check_user

    def _check_team_(team_id: str, db: Session):
        check_team = db.query(TeamsModels).filter(TeamsModels.id == team_id).first()

        if not check_team:
            raise HTTPException(
                status_code=404, detail=f"User not found with {team_id}"
            )

        return check_team

    @staticmethod
    def all_teams(db: Session):
        return db.query(TeamsModels).all()

    @staticmethod
    def get_team_by_id(team_id: str, db: Session):
        team = TeamService._check_team_(team_id, db)
        return team

    @staticmethod
    def create_team(data: TeamsReq, db: Session):
        TeamService._check_org_(data.org_id, db)

        new_team = TeamsModels(**data.model_dump())

        db.add(new_team)
        db.commit()
        db.refresh(new_team)

        return new_team

    @staticmethod
    def add_user_to_team(data: TeamMemberReq, db: Session):
        TeamService._check_org_(data.org_id, db)
        TeamService._check_team_(data.team_id, db)
        TeamService._check_user_(data.user_id, db)

        user_already_exist = (
            db.query(TeamMembersModel)
            .filter(TeamMembersModel.user_id == data.user_id)
            .first()
        )
        if user_already_exist:
            raise HTTPException(
                status_code=400, detail=f"User already registered {data.user_id}"
            )

        new_team_member = TeamMembersModel(**data.model_dump())

        db.add(new_team_member)
        db.commit()
        db.refresh(new_team_member)
        new_team_member.message = "User added successfully"

        return new_team_member

    @staticmethod
    def get_team_member(team_id: str, db: Session):
        TeamService._check_team_(team_id, db)
        data = db.query(TeamMembersModel).filter(TeamMembersModel.is_active).all
        return data

    @staticmethod
    def delete_user_from_team(data: TeamDeleteMember, db: Session):
        TeamService._check_team_(data.team_id, db)
        TeamService._check_user_(data.user_id, db)

        team_member = (
            db.query(TeamMembersModel)
            .filter(
                TeamMembersModel.user_id == data.user_id,
                TeamMembersModel.team_id == data.team_id,
                TeamMembersModel.is_active == True,
            )
            .first()
        )

        if not team_member:
            raise HTTPException(
                status_code=400, detail="User is not a active user in this team"
            )

        team_member.is_active = False

        db.commit()
        db.refresh(team_member)

        return team_member
