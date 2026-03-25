from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

class Login(BaseModel):
    email:str
    password:str

# class UserUpdate(BaseModel):
#     name:str
#     email:str
#     password:str

# class UserDelete(BaseModel):
#     id:int

