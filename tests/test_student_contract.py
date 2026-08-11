from faker import Faker

from services.university.university_helpers.group_helper import GroupHelper
from services.university.university_helpers.student_helper import StudentHelper
from services.university.university_models.base_student import DegreeEnum

faker = Faker()
import random
from logger.logger import Logger


class TestStudentContract:

    def test_create_student(self, university_api_utils_admin):
        Logger.info(f"### Step 1. Create group")
        group = GroupHelper(university_api_utils_admin)
        group_requests = group.post_group({"name": faker.word()})
        group_id = group_requests.json()['id']

        Logger.info(f"### Step 1: Create student")
        student_helper = StudentHelper(university_api_utils_admin)
        student = student_helper.post_student({"first_name": faker.first_name(),
                                               "last_name": faker.last_name(),
                                               "email": faker.email(),
                                               "degree": random.choice([option for option in DegreeEnum]),
                                               "phone": faker.numerify("+7##########"),
                                               "group_id": group_id})

        assert student.status_code == 201, \
            (f"Wrong status code: {student.status_code}",
             f"Assert status code: 422")
