from services.general.base_service import BaseService
from services.university.university_helpers.grade_helper import GradeHelper
from services.university.university_helpers.group_helper import GroupHelper
from services.university.university_helpers.student_helper import StudentHelper
from services.university.university_helpers.teacher_helper import TeacherHelper
from services.university.university_models.grade_request import GradeRequest
from services.university.university_models.grade_response import GradeResponse

from services.university.university_models.grade_status_response import GradeStatisticResponse
from services.university.university_models.group_request import GroupRequest
from services.university.university_models.group_response import GroupResponse
from services.university.university_models.student_request import StudentRequest
from services.university.university_models.student_response import StudentResponse
from services.university.university_models.teacher_delete_response import TeacherDeleteResponse
from services.university.university_models.teacher_request import TeacherRequest
from services.university.university_models.teacher_response import TeacherResponse
from utils.api_utils import ApiUtils


class UniversityService(BaseService):
    SERVICE_URL = "http://localhost:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.teacher_helper = TeacherHelper(self.api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.grade_helper = GradeHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def create_grade(self, grade_request: GradeRequest) -> GradeResponse:
        response = self.grade_helper.post_grade(grade_request.model_dump())
        return GradeResponse(**response.json())

    def get_stats_grade(self, grade_request ) -> GradeStatisticResponse:
        response = self.grade_helper.get_grades_stats(grade_request)
        return GradeStatisticResponse(**response.json())

    def delete_teacher(self, teacher_request ) -> TeacherDeleteResponse:
        response = self.teacher_helper.delete_teacher(teacher_request)
        return TeacherDeleteResponse(**response.json())