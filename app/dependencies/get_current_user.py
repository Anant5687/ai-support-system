from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
import jwt
from jwt.exceptions import InvalidTokenError

from app.models.user_models import UserModel
from app.db.database import get_db

oauth2_scheme = OAuth2PasswordBearer("/users/login")

def get_current_user(token=Depends(oauth2_scheme), db: Session = Depends(get_db)):
    invalid_credentials = HTTPException(
        status_code=404,
        detail="Invalid credentials",
        headers=("WWW-Authentication", "Bearer"),
    )

    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )

        user_id = payload.get("sub")

        if not user_id:
            raise invalid_credentials

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise invalid_credentials

    except InvalidTokenError:
        raise invalid_credentials
    except:
        raise invalid_credentials

    return user
