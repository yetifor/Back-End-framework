from enum import IntEnum

from pydantic import BaseModel


class GradesEnum(IntEnum):
    MIN_GRADE = 0
    MAX_GRADE = 5

class BaseGrade(BaseModel):
    teacher_id: int
    student_id: int
    grade: GradesEnum


