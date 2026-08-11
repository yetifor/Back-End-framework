from enum import IntEnum

from pydantic import BaseModel, Field


MIN_GRADE_VALUE = 0
MAX_GRADE_VALUE = 5


class BaseGrade(BaseModel):
    teacher_id: int
    student_id: int
    grade: int = Field(ge=MIN_GRADE_VALUE, le=MAX_GRADE_VALUE)
