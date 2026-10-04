from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db

from app.services.teams_services import TeamService
from app.schemas.teams_schemas import (
    TeamMemberReq,
    TeamsReq,
    TeamDeleteMember,
    TeamMemberRes,
    TeamsRes,
)

router = APIRouter(prefix="/teams", tags=["teams"])


@router.get("/", response_model=list[TeamsRes])
def get_all_teams(db: Session = Depends(get_db)):
    try:
        return TeamService.all_teams(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.get("/{team_id}", response_model=TeamsRes)
def get_team_by_id(team_id: str, db: Session = Depends(get_db)):
    try:
        return TeamService.get_team_by_id(team_id, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.post("/create", response_model=TeamsRes)
def create_team(data: TeamsReq, db: Session = Depends(get_db)):
    try:
        return TeamService.create_team(data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.post("/add/member", response_model=TeamMemberRes)
def add_user_to_team(data: TeamMemberReq, db: Session = Depends(get_db)):
    try:
        return TeamService.add_user_to_team(data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.get("/{team_id}/member")
def get_team_member(team_id: str, db: Session = Depends(get_db)):
    try:
        return TeamService.get_team_member(team_id, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.delete("/delete/member")
def delete_user_from_team(data: TeamDeleteMember, db: Session = Depends(get_db)):
    try:
        return TeamService.delete_user_from_team(data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )
