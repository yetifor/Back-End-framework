import random

from faker import Faker

from logger.logger import Logger
from services.university.university_helpers.grade_helper import GradeHelper
from services.university.university_models import student_request, grade_response
from services.university.university_models.base_student import DegreeEnum
from services.university.university_models.base_teacher import SubjectEnum
from services.university.university_models.grade_request import GradeRequest
from services.university.university_models.grade_status_request import GradeStatisticRequest
from services.university.university_models.grade_status_response import GradeStatisticResponse
from services.university.university_models.group_request import GroupRequest
from services.university.university_models.group_response import GroupResponse
from services.university.university_models.student_request import StudentRequest
from services.university.university_models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestStatsGrade:

    def test_stats_grade(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        Logger.info("### Step 1. Create group ###")
        group_request = GroupRequest(name=faker.word())
        group_response = university_service.create_group(group_request=group_request)

        Logger.info("### Step 2. Create Student ###")
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice([option for option in
                                                       DegreeEnum]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)

        Logger.info("### Step 3. Create Teacher ###")
        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in
                                                        SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)

        Logger.info("### Step 4. Create Grades ###")
        grade1 = GradeRequest(teacher_id=teacher_response.id,
                              student_id=student_response.id,
                              grade=random.randint(GradeHelper.MIN_GRADE_VALUE, GradeHelper.MAX_GRADE_VALUE + 1))

        grade_response1 = university_service.create_grade(grade_request=grade1)

        grade2 = GradeRequest(teacher_id=teacher_response.id,
                              student_id=student_response.id,
                              grade=random.randint(GradeHelper.MIN_GRADE_VALUE, GradeHelper.MAX_GRADE_VALUE + 1))

        grade_response2 = university_service.create_grade(grade_request=grade2)
        grades = [grade_response1.grade, grade_response2.grade]

        Logger.info("### Step 5. Create Statistics ###")

        grade_stats_request = GradeStatisticRequest(student_id=student_response.id,
                                                    teacher_id=teacher_response.id,
                                                    group_id=group_response.id)
        grade_stats_response = university_service.get_stats_grade(grade_request=grade1)

        expected_avg = sum(grades) / len(grades)

        assert expected_avg == grade_stats_response.avg, \
            (f"Wrong avg actual: {grade_stats_response.avg}, "
             f"Assert avg: {expected_avg}")
