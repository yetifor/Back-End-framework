from services.general.helpers.base_helper import BaseHelper
import requests

class TeacherHelper(BaseHelper):
    END_PREFIX = "/teachers"

    ROOT_ENDPOINT = f"{END_PREFIX}/"

    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response
