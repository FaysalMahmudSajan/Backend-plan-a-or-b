from fastapi import APIRouter,status,Depends,Request
from sqlalchemy.orm import Session
from src.user.dtos import UserCreate,UserResponse,Login
from src.utils.db import get_db
from src.utils.helps import authenticated
from src.user import controller as con 
# from src.utils.password import get,verify_password


user_router=APIRouter(prefix="/user",tags=["User"])

@user_router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register(user:UserCreate,db:Session=Depends(get_db)):
    return con.register_user(user,db)

@user_router.post("/login",status_code=status.HTTP_200_OK)
def login(user:Login,db:Session=Depends(get_db)):
    return con.login_user(user,db)

@user_router.get("/get",response_model=list[UserResponse],status_code=status.HTTP_200_OK)
def get(db:Session=Depends(get_db),user=Depends(authenticated)):
    return con.get_user(db)

@user_router.get("/is_auth", response_model=UserResponse, status_code=status.HTTP_200_OK)
def is_auth(request: Request, db: Session = Depends(get_db)):
    return con.authenticated(request, db)
