from src.user.models import User
from fastapi import HTTPException
from src.utils.helps import verify_password,get_password_hash,create_token,authenticated



def register_user(user,db):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="User already exists")

    new_user = User()
    new_user.name=user.name     
    new_user.email=user.email
    new_user.hash_password=get_password_hash(user.password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(user,db):

    user_login=db.query(User).filter(User.email==user.email).first()
    if not user_login:
        raise HTTPException(status_code=404,detail="User not found")
    if not verify_password(user.password,user_login.hash_password):
        raise HTTPException(status_code=401,detail="Invalid password")
    
    token=create_token(user)

    return token

def get_user(db):
    all_user=db.query(User).all()
    return all_user