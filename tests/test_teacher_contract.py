from services.university.university_helpers.teacher_helper import TeacherHelper
from services.university.university_models.base_teacher import SubjectEnum
from services.university.university_models.teacher_request import TeacherRequest
from faker import Faker

from services.university.university_service import UniversityService

faker = Faker()
import random
from logger.logger import Logger


class TestTeacherContract:
    def test_create_teacher_admin(self, university_api_utils_admin):
        Logger.info(f"### Step 1. Create teacher")
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        teacher = teacher_helper.post_teacher({'first_name': faker.first_name(),
                                               'last_name': faker.last_name(),
                                               'subject': random.choice([option for option in SubjectEnum])})
        assert teacher.status_code == 201, \
            (f"Wrong status code: {teacher.status_code}",
             f"Assert status code: 201",)

    def test_create_teacher_anonym(self, university_api_utils_anonym):
        Logger.info(f"### Step 1. Create teacher")
        teacher_helper = TeacherHelper(api_utils=university_api_utils_anonym)
        teacher = teacher_helper.post_teacher({'first_name': faker.first_name(),
                                               'last_name': faker.last_name(),
                                               'subject': random.choice([option for option in SubjectEnum])})
        assert teacher.status_code == 403, \
            (f"Wrong status code: {teacher.status_code}",
             f"Assert status code: 403",)

    def test_teacher_delete(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        Logger.info("### Step 1. Create Teacher ###")
        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in
                                                        SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)

        teacher_id = teacher_response.id
        Logger.info(f"### Step 2. Delete teacher")
        teacher_response = university_service.delete_teacher(teacher_request=teacher_id)

        assert teacher_response.detail == "Teacher deleted", \
            (f"Wrong status code: {teacher_response.detail}",
             f"But expected: 'Teacher deleted'")

    def test_teacher_artifice_delete(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        Logger.info("### Step 1. Create Teacher ###")
        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in
                                                        SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)

        teacher_id = teacher_response.id
        Logger.info(f"### Step 2. Delete teacher")
        teacher_response = university_service.delete_teacher(teacher_request=
                                                             (teacher_id + 999999999999))

        assert teacher_response.detail == "Teacher not found", \
            (f"Wrong status code: {teacher_response.detail}",
             f"But expected: 'Teacher not found'")

    def test_teacher_create_fake_subject(self, university_api_utils_admin):
        Logger.info(f"### Step 1. Create teacher")
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        teacher = teacher_helper.post_teacher({'first_name': faker.first_name(),
                                               'last_name': faker.last_name(),
                                               'subject': faker.word()})

        assert teacher.status_code == 422, \
            (f"Wrong status code: {teacher.status_code}",
             f"Assert status code: 422")
