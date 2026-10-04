from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.organisation_schemas import (
    OrganisationRes,
    OrganisationReq,
    OrganisationMemberRes,
    OrganisationMemberReq,
)
from app.db.database import get_db
from app.services.organisation_service import OrganisationService

router = APIRouter(prefix="/organisation", tags=["Organisation"])


@router.get("/", response_model=list[OrganisationRes])
def get_all_org(db: Session = Depends(get_db)):
    try:
        return OrganisationService.get_all_org(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.post("/create", response_model=OrganisationRes)
def create_org(data: OrganisationReq, db: Session = Depends(get_db)):
    try:
        return OrganisationService.create_org(data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.post("/add/member", response_model=OrganisationMemberRes)
def add_member_to_org(data: OrganisationMemberReq, db: Session = Depends(get_db)):
    try:
        return OrganisationService.add_user_to_org(data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.get("/{org_id}", response_model=OrganisationRes)
def get_org(org_id: str, db: Session = Depends(get_db)):
    try:
        return OrganisationService.get_organisation(org_id, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.get("/{org_id}/members", response_model=list[OrganisationMemberRes])
def get_org(org_id: str, db: Session = Depends(get_db)):
    try:
        return OrganisationService.org_members(org_id, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )
