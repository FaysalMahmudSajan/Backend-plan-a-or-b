from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.db import Base,engine
from src.task.router import task_router
from src.user.router import user_router

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://github.com/FaysalMahmudSajan"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000 ,reload=True)


