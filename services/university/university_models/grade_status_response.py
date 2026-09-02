from pydantic import BaseModel, Field
from services.university.university_models.base_grade import BaseGrade
from typing import ClassVar
from services.university.university_models.base_grade import MIN_GRADE_VALUE, MAX_GRADE_VALUE

class GradeStatisticResponse(BaseModel):
    count: int = Field(ge=0)
    min: int | None = Field(ge=MIN_GRADE_VALUE, le=MAX_GRADE_VALUE)
    max: int | None = Field(ge=MIN_GRADE_VALUE, le=MAX_GRADE_VALUE)
    avg: float | None = Field(ge=MIN_GRADE_VALUE, le=MAX_GRADE_VALUE)
