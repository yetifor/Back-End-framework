from services.general.helpers.base_helper import BaseHelper
import requests

class TeacherHelper(BaseHelper):
    END_PREFIX = "/teachers"

    ROOT_ENDPOINT = f"{END_PREFIX}/"

    TEACHER_ID_ENDPOINT = f"{END_PREFIX}{{TeacherId}}"
    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.delete(f"{self.ROOT_ENDPOINT}{teacher_id}")
        return response
