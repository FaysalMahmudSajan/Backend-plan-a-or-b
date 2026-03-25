from fastapi import HTTPException,status,Request,Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from src.utils.settings import settings
from src.utils.db import get_db
from pwdlib import PasswordHash
from src.user.models import User
import jwt




password_hash = PasswordHash.recommended()
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)


def create_token(user):
    exp_time = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {"email": user.email, "exp": exp_time}
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        settings.ALGORITHM,
    )
    print(f"token: {token}, time: {exp_time}")
    return {"token": token, "time": exp_time}


def authenticated(request:Request, db:Session=Depends(get_db)):
    token = request.headers.get("authorization")
    # print(token)
    # jwt_token = token.split(" ")[-1]
    # print(jwt_token)
    jwt_token = token
    try:
        data = jwt.decode(
            jwt_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print(data)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="Invalid Token")
    user = (
        db.query(User).filter(User.email == data.get("email")).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized Email"
        )
    return user