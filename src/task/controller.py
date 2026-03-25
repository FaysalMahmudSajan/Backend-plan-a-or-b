from src.task.models import TasksModel

def create_task(task,db,auth):
    new_task = TasksModel()

    new_task.title = task.title
    new_task.description = task.description
    new_task.status = task.status
    new_task.user_id = auth.id

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks(db,auth):
    return db.query(TasksModel).filter(TasksModel.user_id == auth.id).all()

def get_task_by_id(id,db,auth):
    return db.query(TasksModel).filter(TasksModel.id == id,TasksModel.user_id == auth.id).first()

def update_task(id,task,db,auth):
    update_task = db.query(TasksModel).filter(TasksModel.id == id,TasksModel.user_id == auth.id).first()
    update_task.title = task.title
    update_task.description = task.description
    update_task.status = task.status

    db.commit()
    db.refresh(update_task)
    return update_task

def delete_task(id,db,auth):
    delete_task = db.query(TasksModel).filter(TasksModel.id == id,TasksModel.user_id == auth.id).first()
    db.delete(delete_task)
    db.commit()
    return delete_task
