from pydantic import BaseModel, Field
from services.university.university_models.base_grade import BaseGrade
from typing import ClassVar

class GradeStatisticResponse(BaseModel):
    MIN_GRADE: ClassVar[int] = 0
    MAX_GRADE: ClassVar[int] = 5
    count: int = Field(ge=0)
    min: int | None = Field(ge=MIN_GRADE, le=MAX_GRADE)
    max: int | None = Field(ge=MIN_GRADE, le=MAX_GRADE)
    avg: float | None = Field(ge=MIN_GRADE, le=MAX_GRADE)
