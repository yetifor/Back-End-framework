from pydantic import BaseModel, Field

from services.university.university_models.base_grade import MIN_GRADE_VALUE, MAX_GRADE_VALUE


class ExpectedModel(BaseModel):

    expected_count : int = Field(ge=0)
    expected_avg : float | None = Field(ge=MIN_GRADE_VALUE, le=MAX_GRADE_VALUE)
    expected_min : int | None = Field(ge=MIN_GRADE_VALUE, le=MAX_GRADE_VALUE)
    expected_max : int | None = Field(ge=MIN_GRADE_VALUE, le=MAX_GRADE_VALUE)
