import requests

from services.general.helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    END_PREFIX = "/users"

    ME_ENDPOINT = f"{END_PREFIX}/me"


    def get_me(self)->requests.Response:
        response = self.api_utils.get(self.ME_ENDPOINT)
        return response