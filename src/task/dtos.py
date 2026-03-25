from pydantic import BaseModel

class TaskCreate(BaseModel):
    
    title: str
    description: str
    status: bool=False
    # user_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: bool