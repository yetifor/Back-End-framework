from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class SubjectEnum(StrEnum):
    MATH = "Mathematics"
    PHYS = "Physics"
    HIST = "History"
    BIO = "Biology"
    GEO = "Geography"


class BaseTeacher(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    subject: SubjectEnum
