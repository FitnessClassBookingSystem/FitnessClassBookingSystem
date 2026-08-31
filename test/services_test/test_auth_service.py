import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fitness_booking.dtos.request.login_user_request import LoginUserRequest
from fitness_booking.dtos.request.logout_user_request import LogoutUserRequest
from fitness_booking.dtos.request.register_user_request import RegisterUserRequest
from fitness_booking.models.user_model import Base
from fitness_booking.repositories.mysql_user_repository import MySQLUserRepository
from fitness_booking.services.auth_service import AuthService, InvalidPasswordError, UserNotFoundError

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine("mysql+pymysql://root:LUCID1212@localhost/fitness_class_booking_system")
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

class TestAuthService:
    def setup_method(self):
        self.db = SessionLocal()

    def test_userCanRegister(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = RegisterUserRequest(username="lucid", email="semicolon@gmail.com", password="LUCID1212")
        response = process.register(user_request)
        assert response.message == "User registered successfully."


    def test_multipleUsers_canRegister(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = RegisterUserRequest(username="cartel", email="cartel@gmail.com", password="CARTEL1212")
        user2_request = RegisterUserRequest(username="luca", email="shot@gmail.com", password="LUCA_JONES")
        response = process.register(user_request)
        assert response.message == "User registered successfully."
        response = process.register(user2_request)
        assert response.message == "User registered successfully."


    def test_userCannotRegister_withExistingUsername(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = RegisterUserRequest(username="cartel", email="new@gmail.com", password="CARTEL")
        with pytest.raises(Exception):
            response = process.register(user_request)
        assert user_repository.count() == 3


    def test_userCanRegister_withExistingEmail(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = RegisterUserRequest(username="zion", email="semicolon@gmail.com", password="people")
        response = process.register(user_request)
        assert user_repository.count() == 4


    # def test_userPassword_cannot_exceed15Characters(self):
    #     user_repository = MySQLUserRepository(self.db)
    #     process = AuthService(user_repository)
    #     user_request = RegisterUserRequest(username="lucid", email="password@gmail.com", password="thisatestingpasswordjusttotestthepasswordlimit")
    #     response = process.register(user_request)
    #     assert response.message != "User registered successfully."

    def test_userPassword_mustBeUpToThegivenConstraint(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = RegisterUserRequest(username="lucid", email="password@gmail.com", password="PASS")
        with pytest.raises(InvalidPasswordError):
            process.register(user_request)


    def test_userCanLogin(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = LoginUserRequest(username="lucid", password="LUCID1212")
        response = process.login(user_request)
        assert response.message == "Login successful."


    def test_userCannotLogin_withInvalidPassword(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = LoginUserRequest(username="lucid", password="lucid1212")
        with pytest.raises(UserNotFoundError):
            process.login(user_request)

    def test_userCannotLogin_withInvalidUsername(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = LoginUserRequest(username="lucy", password="LUCID1212")
        with pytest.raises(UserNotFoundError):
            process.login(user_request)


    def test_username_isNotCaseSensitive(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = LoginUserRequest(username="luCId", password="LUCID1212")
        response = process.login(user_request)
        assert response.message == "Login successful."


    def test_userCanLogout(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = LogoutUserRequest(username="lucid")
        response = process.logout(user_request)
        assert response.message == "Logout successful."


    def test_userCannotLogout_withInvalidUsername(self):
        user_repository = MySQLUserRepository(self.db)
        process = AuthService(user_repository)
        user_request = LogoutUserRequest(username="luciid")
        with pytest.raises(UserNotFoundError):
            process.logout(user_request)