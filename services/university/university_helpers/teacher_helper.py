from services.general.helpers.base_helper import BaseHelper
import requests

from services.university.university_models.teacher_delete_response import TeacherDeleteResponse
from services.university.university_models.teacher_response import TeacherResponse


class TeacherHelper(BaseHelper):
    END_PREFIX = "/teachers"

    ROOT_ENDPOINT = f"/teachers/"



    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.delete(f"{self.END_PREFIX}/{teacher_id}")
        return response
