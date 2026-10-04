from sqlalchemy.orm import Session
from app.schemas.users_schemas import UserCreateReq, LoginReq
from app.models.user_models import UserModel
from app.core.security import hash_password, create_token, verify_password

from fastapi import HTTPException


class UserService:
    @staticmethod
    def create_user(data: UserCreateReq, db: Session):
        password_hash = hash_password(data.password)
        new_user = UserModel(**data.model_dump())
        new_user.password = password_hash

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def login_user(data: LoginReq, db: Session):
        user_exist = db.query(UserModel).filter(UserModel.email == data.email).first()

        if not user_exist:
            raise HTTPException(
                status_code=404, detail=f"User not found with: {data.email}"
            )

        password_verify = verify_password(data.password, user_exist.password)

        if not password_verify:
            raise HTTPException(status_code=400, detail="Bad credentials")

        if not user_exist.is_active:
            raise HTTPException(status_code=403, detail="User is not active")

        access_token = create_token(user_exist.id)
        user_exist.access_token = access_token
        user_exist.token_type = "Bearer"
        return user_exist
