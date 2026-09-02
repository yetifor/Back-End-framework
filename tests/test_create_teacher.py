from logger.logger import Logger
from services.university.university_models.base_teacher import SubjectEnum
from services.university.university_models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from faker import Faker

faker = Faker()
import random


class TestCreateTeacher:
    def test_teacher(self, university_api_utils_admin):
        Logger.info(f"### Step 1. Create teacher")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in
                                                        SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)

        assert teacher.first_name == teacher_response.first_name, \
            (f"Wrong first_name actual: {teacher.first_name}",)
