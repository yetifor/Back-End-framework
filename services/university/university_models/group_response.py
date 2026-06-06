from pydantic import BaseModel, ConfigDict


class GroupResponse(BaseModel):
    id: int
