import random

import faker
import requests
import pytest
from faker import Faker

from logger.logger import Logger
from services.university.university_helpers.group_helper import GroupHelper
from services.university.university_helpers.student_helper import StudentHelper
from services.university.university_models.base_student import DegreeEnum

faker = Faker()


class TestGroupContract:

    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code: {response.status_code}"
             f"But expected status code: {requests.status_codes.codes.ok}")

    def test_create_group_admin(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.post_group({"name": faker.name()})

        assert response.status_code == 201, \
            (f"Wrong status code: {response.status_code}"
             f"But expected status code: {requests.status_codes.codes.ok}")

    def test_group_delete(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        Logger.info(f"### Step 1. Create group")
        response = group_helper.post_group({"name": faker.name()})
        Logger.info(f"### Step 2. Get group ID")
        group_id = response.json()["id"]
        Logger.info(f"### Step 3. Delete group")
        group_delete = group_helper.delete_group(group_id)

        assert group_delete.status_code == 200, \
            (f"Wrong status code: {group_delete.status_code}"
             f"But expected status code: {requests.status_codes.codes.ok}")

    def test_group_register_empty_field(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        Logger.info(f"### Step 1. Create group")
        response = group_helper.post_group({"name": None})
        assert response.status_code == 422, \
            (f"Wrong status code: {response.status_code}"
             f"But expected status code: 422")

    def test_group_add_invalid_student_id(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)

        Logger.info(f"### Step 1. Create group")
        response = group_helper.post_group({"name": faker.name()})

        Logger.info(f"### Step 2. Get group ID")
        group_id = response.json()["id"]

        Logger.info(f"### Step 3. Create Student")
        student_helper = StudentHelper(university_api_utils_admin)
        student = student_helper.post_student({"first_name": faker.first_name(),
                                               "last_name": faker.last_name(),
                                               "email": faker.email(),
                                               "degree": random.choice([option for option in DegreeEnum]),
                                               "phone": faker.numerify("+7##########"),
                                               "group_id": "invalid_group_id"})

        assert student.status_code == 422, \
            (f"Wrong status code: {student.status_code}"
             f"But expected status code: 422")
