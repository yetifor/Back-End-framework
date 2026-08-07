from pydantic import BaseModel, ConfigDict


class GradeStatisticRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    student_id: int | None
    teacher_id: int | None
    group_id: int | None

