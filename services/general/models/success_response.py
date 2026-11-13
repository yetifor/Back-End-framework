from pydantic import BaseModel, ConfigDict, EmailStr


class SuccessResponse(BaseModel):

    detail:str