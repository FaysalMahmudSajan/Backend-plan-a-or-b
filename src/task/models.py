from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from src.utils.db import Base

class TasksModel(Base):
    __tablename__ = "tasks_table"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description = Column(String)
    status = Column(Boolean,default=False)
    user_id = Column(Integer,ForeignKey("users_table.id",ondelete="CASCADE"))