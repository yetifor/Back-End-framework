from pydantic import BaseModel


class TeacherDeleteResponse(BaseModel):
    detail: str
