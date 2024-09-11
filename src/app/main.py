from fastapi import FastAPI
from app.routers import tasks, users

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    title="Task manager API",
    description="Opis mojego API",
    version="3.1.0",
)


@app.get("/")
def root():
    return "hello world"


app.include_router(tasks.router)
app.include_router(users.router)
