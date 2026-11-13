import requests

from services.general.helpers.base_helper import BaseHelper
from utils.api_utils import ApiUtils


class AuthorizationHelper(BaseHelper):

    END_PREFIX = "/auth"
    LOGIN_END = f"{END_PREFIX}/login/"
    REGISTER_END = f"{END_PREFIX}/register/"


    def post_register(self, data: dict)->requests.Response:
        response = self.api_utils.post(self.REGISTER_END, data=data)
        return response

    def post_login(self, data: dict)->requests.Response:
        response = self.api_utils.post(self.LOGIN_END, data=data)
        return response