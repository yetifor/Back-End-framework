import requests
from services.university.university_models.grade_status_response import GradeStatisticResponse
from services.general.helpers.base_helper import BaseHelper
from services.university.university_models.grade_request import GradeRequest
from services.university.university_models.grade_response import GradeResponse
from services.university.university_models.grade_status_response import GradeStatisticResponse
from services.university.university_models.stats_expected_model import ExpectedModel


class GradeHelper(BaseHelper):
    END_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{END_PREFIX}/"
    STATS_ENDPOINT = f"{END_PREFIX}/stats/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grades_stats(self, student_id=None, teacher_id=None, group_id=None) -> requests.Response:
        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id

        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response

    def clean_statistics(self, count: int) -> None:
        for i in range(count + 1):
            grade_id = i
            response = self.api_utils.delete(f"{self.ROOT_ENDPOINT}{grade_id}")

        return None
