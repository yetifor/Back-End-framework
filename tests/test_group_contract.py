import requests
import pytest
from faker import Faker

from logger.logger import Logger
from services.university.university_helpers.group_helper import GroupHelper

fake = Faker()


class TestGroupContract:

    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": fake.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code: {response.status_code}"
             f"But expected status code: {requests.status_codes.codes.ok}")

    def test_create_group_admin(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.post_group({"name": fake.name()})

        assert response.status_code == 201, \
            (f"Wrong status code: {response.status_code}"
             f"But expected status code: {requests.status_codes.codes.ok}")

    def test_group_delete(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        Logger.info(f"### Step 1. Create group")
        response = group_helper.post_group({"name": fake.name()})
        Logger.info(f"### Step 2. Get group ID")
        group_id = response.json()["id"]
        Logger.info(f"### Step 3. Delete group")
        group_delete = group_helper.delete_group(group_id)

        assert group_delete.status_code == 200, \
            (f"Wrong status code: {group_delete.status_code}"
             f"But expected status code: {requests.status_codes.codes.ok}")
