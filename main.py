from fastapi import FastAPI, Body
from pydantic import BaseModel, PositiveInt, model_validator, constr


app = FastAPI()


class TaskBody(BaseModel):
    """
    TaskBody jest modelem request body używanym w endpoincie POST /tasks
    Waliduje on poprawność użytego w requeście body
    """
    description: str
    priority: PositiveInt  # int | None = None  # dopuszczamy też None i None jest domyślne
    is_complete: bool = False  # domyślnie jest False

    @model_validator(mode="after")
    def validate(self):
        """
        mode - after/before mówi o tym czy walidator odpala się przed walidacją
                typów czy po
        Tutaj odbywa się bardziej zaawansowana walidacja modelu danych
        Przyjmujemy i zwracamy self
        """
        # if len(self.description) > self.priority:
        #     raise AssertionError("Description must be less than priority")
        return self


class UserBody(BaseModel):
    username: str
    password: constr(min_length=8)
    is_admin: bool = False


tasks_data = [
    {"id": 1, "description": "Learn FastAPI", "priority": 3, "is_complete": True},
    {"id": 2, "description": "Do exercises", "priority": 2, "is_complete": False}
]

users_data = [
    {"id": 1, "username": "Andrzej", "password": "qwerty123", "is_admin": True},
    {"id": 2, "username": "Andżela", "password": "hasło1!", "is_admin": False},
]


@app.get("/")
def root():
    return "hello world"


@app.get("/tasks")
def get_tasks():
    return {"result": tasks_data}


@app.post("/tasks")
def create_task(body: TaskBody):
    new_task = body.model_dump()
    task_id = len(tasks_data) + 1
    new_task["id"] = task_id

    tasks_data.append(new_task)

    return {"message": "New task added",
            "details": new_task}


@app.get("/users/")
def get_users():
    return {"result": users_data}


@app.post("/users/")
def create_user(body: UserBody):
    new_user = body.model_dump()
    user_id = len(users_data) + 1
    new_user["id"] = user_id
    users_data.append(new_user)

    return {"message": "New user added", "details": new_user}
