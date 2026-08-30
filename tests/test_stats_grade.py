import random

from faker import Faker

from logger.logger import Logger
from services.university.university_models.base_grade import MAX_GRADE_VALUE, MIN_GRADE_VALUE
from services.university.university_helpers.grade_helper import GradeHelper
from services.university.university_models import student_request, grade_response
from services.university.university_models.base_student import DegreeEnum
from services.university.university_models.base_teacher import SubjectEnum
from services.university.university_models.grade_request import GradeRequest
from services.university.university_models.stats_expected_model import ExpectedModel
from services.university.university_models.stats_actual_model import ActualModel
from services.university.university_models.grade_status_response import GradeStatisticResponse
from services.university.university_models.group_request import GroupRequest
from services.university.university_models.group_response import GroupResponse
from services.university.university_models.student_request import StudentRequest
from services.university.university_models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.soft_assert import SoftAssert

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

        Logger.info("### Step 4. Create Grades###")
        grade = 2

        grade1 = GradeRequest(teacher_id=teacher_response.id,
                              student_id=student_response.id,
                              grade=2)
        grade1_response = university_service.create_grade(grade_request=grade1)

        grade2 = GradeRequest(teacher_id=teacher_response.id,
                              student_id=student_response.id,
                              grade=3)
        grade2_response = university_service.create_grade(grade_request=grade2)

        grade_stats = university_service.get_stats_grade(student_id=student_response.id,
                                                         teacher_id=teacher_response.id,
                                                         group_id=group_response.id)

        grades = [grade1_response.grade, grade2_response.grade]

        Logger.info("### Step 5. Create Statistics ###")

        expected_count = len(grades)
        expected_avg = sum(grades) / len(grades)
        expected_min = min(grades)
        expected_max = max(grades)

        with SoftAssert() as sa:
            sa.soft_assert(grade_stats.count, expected_count, "Test count")
            sa.soft_assert(grade_stats.avg, expected_avg, "Test avg")
            sa.soft_assert(grade_stats.min, expected_min, "Test min")
            sa.soft_assert(grade_stats.max, expected_max, "Test max")

    def test_stats_empty_teacher(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        Logger.info("### Step 1. Create Teacher ###")
        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in
                                                        SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)

        stats = university_service.get_stats_grade(teacher_id=teacher_response.id)


        expected_model = ExpectedModel(expected_count=0,
                                       expected_avg=None,
                                       expected_min=None,
                                       expected_max=None)

        actual_model = ExpectedModel(expected_count=stats.count,
                                   expected_avg=stats.avg,
                                   expected_min=stats.min,
                                   expected_max=stats.max)
        assert expected_model == actual_model, \
            (f" {expected_model} != {actual_model}",)

    def test_stats_invalid_teacher(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        stats = university_service.get_stats_grade(
            teacher_id=random.randint(5000000, 100000000))

        expected_count = stats.count
        expected_avg = None
        expected_min = None
        expected_max = None

        with SoftAssert() as sa:
            sa.soft_assert(stats.count, expected_count, "Test count")
            sa.soft_assert(stats.avg, expected_avg, "Test avg")
            sa.soft_assert(stats.min, expected_min, "Test min")
            sa.soft_assert(stats.avg, expected_max, "Test max")

    def test_stats_not_found_student(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        stats = university_service.get_stats_grade(student_id=random.randint(122222, 99999999), )

        expected_count = stats.count
        expected_avg = None
        expected_min = None
        expected_max = None

        with SoftAssert() as sa:
            sa.soft_assert(stats.count, expected_count, "Test count")
            sa.soft_assert(stats.avg, expected_avg, "Test avg")
            sa.soft_assert(stats.min, expected_min, "Test min")
            sa.soft_assert(stats.avg, expected_max, "Test max")

    def test_stats_techer(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        Logger.info("### Step 1. Create group ###")
        group_request = GroupRequest(name=faker.word())
        group_response = university_service.create_group(group_request=group_request)

        Logger.info("### Step 2. Create trash Student ###")

        trash_student = StudentRequest(first_name=faker.first_name(),
                                       last_name=faker.last_name(),
                                       email=faker.email(),
                                       degree=random.choice([option for option in
                                                             DegreeEnum]),
                                       phone=faker.numerify("+7##########"),
                                       group_id=group_response.id)
        trash_student_response = university_service.create_student(student_request=trash_student)
        Logger.info("### Step 3. Create trash teacher ###")
        trash_teacher = TeacherRequest(first_name=faker.first_name(),
                                       last_name=faker.last_name(),
                                       subject=random.choice([option for option in
                                                              SubjectEnum]))
        trash_teacher_response = university_service.create_teacher(teacher_request=trash_teacher)
        Logger.info("### Step 4. Create trash grades ###")
        trash_grade1 = GradeRequest(teacher_id=trash_teacher_response.id,
                                    student_id=trash_student_response.id,
                                    grade=4)
        trash_grade1_response = university_service.create_grade(grade_request=trash_grade1)

        trash_grade2 = GradeRequest(teacher_id=trash_teacher_response.id,
                                    student_id=trash_student_response.id,
                                    grade=5)
        grade2_response = university_service.create_grade(grade_request=trash_grade2)

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

        Logger.info("### Step 4. Create Grades###")

        grade1 = GradeRequest(teacher_id=teacher_response.id,
                              student_id=student_response.id,
                              grade=2)
        grade1_response = university_service.create_grade(grade_request=grade1)

        grade2 = GradeRequest(teacher_id=teacher_response.id,
                              student_id=student_response.id,
                              grade=3)
        grade2_response = university_service.create_grade(grade_request=grade2)

        grade_stats = university_service.get_stats_grade(teacher_id=teacher_response.id, )

        grades = [grade1_response.grade, grade2_response.grade]

        Logger.info("### Step 5. Create Statistics ###")

        stats = university_service.get_stats_grade(teacher_id=teacher_response.id, )

        expected_model = ExpectedModel(expected_count=len(grades),
                                       expected_avg=sum(grades) / len(grades),
                                       expected_min=min(grades),
                                       expected_max=max(grades))

        actual_model = ActualModel(expected_count=stats.count,
                                   expected_avg=stats.avg,
                                   expected_min=stats.min,
                                   expected_max=stats.max)

        with SoftAssert() as sa:
            sa.soft_assert(actual_model.expected_count, expected_model.expected_count, "Test count")
            sa.soft_assert(actual_model.expected_avg, expected_model.expected_avg, "Test avg")
            sa.soft_assert(actual_model.expected_min, expected_model.expected_min, "Test min")
            sa.soft_assert(actual_model.expected_max, expected_model.expected_max, "Test max")

    def test_stats_not_found(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        stats = university_service.get_stats_grade()
        cleaner = university_service.clean_statistics(300)

        stats = university_service.get_stats_grade()

        expected_count = stats.count
        expected_avg = None
        expected_min = None
        expected_max = None

        with SoftAssert() as sa:
            sa.soft_assert(stats.count, expected_count, f"Test count")
            sa.soft_assert(stats.avg, expected_avg, f"Test avg/Actual count: {stats.count}")
            sa.soft_assert(stats.min, expected_min, "Test min")
            sa.soft_assert(stats.avg, expected_max, "Test max")
