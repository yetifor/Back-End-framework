from enum import IntEnum

from pydantic import BaseModel, Field




class BaseGrade(BaseModel):
    teacher_id: int
    student_id: int
    grade: int = Field(ge=0, le=5)


