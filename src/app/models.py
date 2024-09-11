from pydantic import BaseModel, PositiveInt, model_validator, constr


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
