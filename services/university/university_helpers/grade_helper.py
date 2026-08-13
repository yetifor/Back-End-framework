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
        params = {'student_id': student_id, 'teacher_id': teacher_id, 'group_id': group_id}
        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response

    def comparison_expected_and_actual_models(self, expected_model, actual_model) -> requests.Response:
        result = (expected_model == actual_model)
        return result