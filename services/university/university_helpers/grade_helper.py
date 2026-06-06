import requests

from services.general.helpers.base_helper import BaseHelper
from services.university.university_models.grade_request import GradeRequest
from services.university.university_models.grade_response import GradeResponse


class GradeHelper(BaseHelper):
    END_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{END_PREFIX}/"

    def post_grade(self, data:dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data= data)
        return response
