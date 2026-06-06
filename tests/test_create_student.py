import random

from services.university.university_models.base_student import DegreeEnum
from services.university.university_models.group_request import GroupRequest
from services.university.university_models.student_request import StudentRequest
from services.university.university_service import UniversityService
import requests
from faker import Faker

faker = Faker()
from logger.logger import Logger


class TestStudent:
    def test_student_create(self, university_api_utils_admin):
        Logger.info("### Step 1. Create group ###")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)

        Logger.info("### Step 2. Create student ###")
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice([option for option in
                                                       DegreeEnum]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)
        Logger.info("### Step 3. Assert ###")
        assert student.group_id == group_response.id, \
            (f"Wrong group id.Actual: '{student_response.group_id}',"
             f" but expected:'{group_response.id}'")
