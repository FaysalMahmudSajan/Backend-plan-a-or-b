from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.task.dtos import TaskCreate,TaskResponse
from src.task.models import TasksModel
from src.task import controller
from src.user.models import User
from src.utils.helps import authenticated

task_router = APIRouter(prefix='/tasks',tags=['task'])

@task_router.post("/create",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(task:TaskCreate,db:Session=Depends(get_db),auth:User=Depends(authenticated)):
    return controller.create_task(task,db,auth)

@task_router.get("/get_all_tasks",response_model=list[TaskResponse],status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session=Depends(get_db),auth:User=Depends(authenticated)):
    return controller.get_all_tasks(db,auth)

@task_router.get("/get_task_by_id/{task_id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int,db:Session=Depends(get_db),auth:User=Depends(authenticated)):
    return controller.get_task_by_id(task_id,db,auth)

@task_router.put("/update_task/{task_id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def update_task(task_id:int,task:TaskCreate,db:Session=Depends(get_db),auth:User=Depends(authenticated)):
    return controller.update_task(task_id,task,db,auth)

@task_router.delete("/delete_task/{task_id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def delete_task(task_id:int,db:Session=Depends(get_db),auth:User=Depends(authenticated)):
    return controller.delete_task(task_id,db,auth)


