from pydantic import BaseModel, Field


class GradeStatisticResponse(BaseModel):
    count: int = Field(ge=0)
    min: int | None
    max: int | None
    avg: float | None