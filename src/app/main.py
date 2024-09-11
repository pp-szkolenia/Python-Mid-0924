from fastapi import FastAPI
from app.routers import tasks, users

app = FastAPI()


@app.get("/")
def root():
    return "hello world"


app.include_router(tasks.router)
app.include_router(users.router)
