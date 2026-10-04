from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.users_services import UserService
from app.schemas.users_schemas import UserCreateRes, LoginRes, LoginReq, UserCreateReq

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create", response_model=UserCreateRes)
def create_user(data: UserCreateReq, db: Session = Depends(get_db)):
    try:
        return UserService.create_user(data, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )


@router.post("/login", response_model=LoginRes)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    try:
        user = UserService.login_user(
            LoginReq(email=form_data.username, password=form_data.password), db
        )
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"{str(e) or "Internal server error"}"
        )
