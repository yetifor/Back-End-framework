from pydantic import BaseModel
from typing import Literal

class LoginResponse(BaseModel):

    access_token: str
    token_type: Literal["Bearer"]
