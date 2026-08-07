import requests
from services.university.university_models.grade_status_response import GradeStatisticResponse
from services.general.helpers.base_helper import BaseHelper
from services.university.university_models.grade_request import GradeRequest
from services.university.university_models.grade_response import GradeResponse
from services.university.university_models.grade_status_response import GradeStatisticResponse


class GradeHelper(BaseHelper):

    MIN_GRADE_VALUE = 0
    MAX_GRADE_VALUE = 5
    END_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{END_PREFIX}/"
    STATS_ENDPOINT = f"{END_PREFIX}/stats/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_stats(self, data: dict) -> requests.Response:
        response = self.api_utils.get(self.STATS_ENDPOINT, data=data)
        return response

    def get_grades_stats(self, params: dict) -> requests.Response:
        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response