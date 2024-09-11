from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, PositiveInt, model_validator, constr
from fastapi.responses import JSONResponse


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


def get_item_by_id(items: list, id_: int):
    for item in items:
        if item["id"] == id_:
            result = item
            break
    else:
        result = None

    return result


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
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"result": tasks_data})


@app.get("/tasks/{id_}")
def get_task_by_id(id_: int):
    target_task = get_item_by_id(tasks_data, id_)
    if target_task is None:
        message = {"error": f"Task with id {id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return {"result": target_task}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(body: TaskBody):
    new_task = body.model_dump()
    task_id = len(tasks_data) + 1
    new_task["id"] = task_id

    tasks_data.append(new_task)

    return {"message": "New task added", "details": new_task}


@app.get("/users/")
def get_users():
    return {"result": users_data}


@app.get("/users/{id_}")
def get_user_by_id(id_: int):
    target_user = get_item_by_id(users_data, id_)
    if target_user is None:
        message = {"error": f"User with id {id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return {"result": target_user}


@app.post("/users/")
def create_user(body: UserBody):
    new_user = body.model_dump()
    user_id = len(users_data) + 1
    new_user["id"] = user_id
    users_data.append(new_user)

    return {"message": "New user added", "details": new_user}
