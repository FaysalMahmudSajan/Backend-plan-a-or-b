from src.utils.db import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__="users_table"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    hash_password=Column(String)