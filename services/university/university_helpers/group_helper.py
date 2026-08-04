import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    END_PREFIX = "/groups"

    ROOT_ENDPOINT = f"{END_PREFIX}/"

    def post_group(self, json: dict)->requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_group(self, group_id: str):
        response = self.api_utils.delete(f"{self.ROOT_ENDPOINT}{group_id}")
        return response