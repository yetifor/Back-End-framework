from logger.logger import Logger
from services.university.university_helpers.grade_helper import GradeHelper
from services.university.university_models.base_grade import MIN_GRADE_VALUE, MAX_GRADE_VALUE
from services.university.university_models.base_student import DegreeEnum
from services.university.university_models.base_teacher import SubjectEnum
from services.university.university_models.grade_request import GradeRequest
from services.university.university_models.group_request import GroupRequest
from services.university.university_models.student_request import StudentRequest
from services.university.university_models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from faker import Faker

import random

faker = Faker()


class TestGrade:
    def test_create_grade(self, university_api_utils_admin):
        Logger.info(f"### Step 1. Create Group ###")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)

        Logger.info(f"### Step 2. Create Student ###")
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice([option for option in
                                                       DegreeEnum]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)

        Logger.info(f"### Step 3. Create Teacher ###")
        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in
                                                        SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)

        grade = GradeRequest(teacher_id=teacher_response.id,
                             student_id=student_response.id,
                             grade=random.randint(MIN_GRADE_VALUE, MAX_GRADE_VALUE + 1))

        grade_response = university_service.create_grade(grade_request=grade)

        assert grade_response.grade == grade.grade, \
            (f"Wrong grade actual: {grade_response.grade}, "
             f"Assert grade: {grade.grade}")
