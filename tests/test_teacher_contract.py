from services.university.university_helpers.teacher_helper import TeacherHelper
from services.university.university_models.base_teacher import SubjectEnum
from services.university.university_models.teacher_request import TeacherRequest
from faker import Faker

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
        Logger.info(f"### Step 1. Create teacher")
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        teacher = teacher_helper.post_teacher({'first_name': faker.first_name(),
                                               'last_name': faker.last_name(),
                                               'subject': random.choice([option for option in SubjectEnum])})

        teacher_id = teacher.json()['id']
        Logger.info(f"### Step 2. Delete teacher")
        teacher_delete = teacher_helper.delete_teacher(teacher_id)

        assert teacher_delete.status_code == 200, (f"Wrong status code: {teacher_delete.status_code}",)

    def test_teacher_artifice_delete(self, university_api_utils_admin):
        Logger.info(f"### Step 1. Create teacher")
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        teacher = teacher_helper.post_teacher({'first_name': faker.first_name(),
                                               'last_name': faker.last_name(),
                                               'subject': random.choice([option for option in SubjectEnum])})

        teacher_id = teacher.json()['id']
        Logger.info(f"### Step 2. Delete teacher")
        teacher_delete = teacher_helper.delete_teacher(teacher_id + random.randint(50, 999))

        assert teacher_delete.status_code == 404, (f"Wrong status code: {teacher_delete.status_code}",)

    def test_teacher_create_fake_subject(self, university_api_utils_admin):
        Logger.info(f"### Step 1. Create teacher")
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        teacher = teacher_helper.post_teacher({'first_name': faker.first_name(),
                                               'last_name': faker.last_name(),
                                               'subject': faker.word()})

        assert teacher.status_code == 422, \
            (f"Wrong status code: {teacher.status_code}",
             f"Assert status code: 422",)
