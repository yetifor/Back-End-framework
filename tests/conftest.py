import random

import psycopg2
import pytest
from faker import Faker
from pydantic import EmailStr

from logger.logger import Logger
from services.auth.auth_service import AuthService
from services.auth.auth_models.login_request import LoginRequest
from services.auth.auth_models.register_request import RegisterRequest
from services.university.university_models.base_student import DegreeEnum
from services.university.university_models.base_teacher import SubjectEnum
from services.university.university_models.group_request import GroupRequest
from services.university.university_models.student_request import StudentRequest
from services.university.university_models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils

faker = Faker()


@pytest.fixture(scope='function', autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope='function', autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope='function', autouse=False)
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()))
    login_response = auth_service.login_user(login_request=LoginRequest(username=username,
                                                                        password=password))
    return login_response.access_token


@pytest.fixture(scope='function', autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope='function', autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils

@pytest.fixture(scope='function', autouse=False)
def create_group(university_api_utils_admin):
    Logger.info("### Factory. Create  group ###")
    university_service = UniversityService(api_utils=university_api_utils_admin)
    group_request = GroupRequest(name=faker.word())
    group = university_service.create_group(group_request=group_request)
    return group

@pytest.fixture(scope='function', autouse=False)
def create_teacher(university_api_utils_admin):
    Logger.info("### Factory. Create  teacher ###")
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher = TeacherRequest(first_name=faker.first_name(),
                                   last_name=faker.last_name(),
                                   subject=random.choice([option for option in
                                                          SubjectEnum]))
    teacher = university_service.create_teacher(teacher_request=teacher)
    return teacher

@pytest.fixture(scope='function', autouse=False)
def create_student(university_api_utils_admin,create_group):
    Logger.info("### Factory. Create  Student ###")
    university_service = UniversityService(api_utils=university_api_utils_admin)
    student = StudentRequest(first_name=faker.first_name(),
                             last_name=faker.last_name(),
                             email=faker.email(),
                             degree=random.choice([option for option in
                                                   DegreeEnum]),
                             phone=faker.numerify("+7##########"),
                             group_id=create_group.id)
    student = university_service.create_student(student_request=student)
    return student

@pytest.fixture(scope="session", autouse=False)
def delete_database():
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=5431,
            dbname="university",
            user="postgres",
            password="1234"
        )
        cursor = conn.cursor()

        cursor.execute("TRUNCATE TABLE teachers, groups, students, grades RESTART IDENTITY CASCADE;")

        conn.commit()
        print("Таблица успешно очищена!")

    except Exception as error:
        print(f"Ошибка: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()


