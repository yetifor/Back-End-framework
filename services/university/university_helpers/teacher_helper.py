import requests

from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    END_PREFIX = "/teachers"

    ROOT_ENDPOINT = "/teachers/"

    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.delete(f"{self.END_PREFIX}/{teacher_id}")
        return response
