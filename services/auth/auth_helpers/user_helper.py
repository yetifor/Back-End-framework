import requests

from services.general.helpers.base_helper import BaseHelper
from utils.api_utils import ApiUtils


class UserHelper(BaseHelper):
    END_PREFIX = "/users"

    ME_ENDPOINT = f"{END_PREFIX}/me"


    def get_me(self)->requests.Response:
        response = self.api_utils.get(self.ME_ENDPOINT)
        return response