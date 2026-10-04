import jwt
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from app.core.config import settings

password_hash = PasswordHash.recommended()


def hash_password(password: str):
    return password_hash.hash(password)


def verify_password(plain_pass: str, hash_pass: str):
    return password_hash.verify(plain_pass, hash_pass)


def create_token(user_id: str):
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {"sub": user_id, "exp": expires_at}
    access_token = jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return access_token
