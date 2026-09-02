from pydantic import BaseModel


class GroupDeleteModel(BaseModel):
    detail: str
