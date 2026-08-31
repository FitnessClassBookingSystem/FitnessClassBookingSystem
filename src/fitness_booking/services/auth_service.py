from fitness_booking.dtos.request.login_user_request import LoginUserRequest
from fitness_booking.dtos.request.logout_user_request import LogoutUserRequest
from fitness_booking.repositories.mysql_user_repository import MySQLUserRepository
from fitness_booking.dtos.request.register_user_request import RegisterUserRequest
from fitness_booking.dtos.response.login_user_response import LoginUserResponse
from fitness_booking.dtos.response.logout_user_response import LogoutUserResponse
from fitness_booking.dtos.response.register_user_response import RegisterUserResponse
from fitness_booking.models.user_model import User


class UserNotFoundError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass


class AuthService:

    def __init__(self, user_storage: MySQLUserRepository):
        self.user_storage = user_storage


    def register(self, user_request: RegisterUserRequest) -> RegisterUserResponse:
        existing_user = self.user_storage.find_by_username(user_request.username)
        if existing_user is not None:
            raise UserNotFoundError('User already exist.')

        user = User(username=user_request.username, email=user_request.email, password=user_request.password)
        self.user_storage.save(user)
        user_response = RegisterUserResponse(message="User registered successfully.")
        return user_response


    def login(self, login_request: LoginUserRequest) -> LoginUserResponse:
        existing_user = self.user_storage.find_by_username(login_request.username)
        if existing_user is None:
            raise UserNotFoundError('Username not found.')
        if existing_user.password != login_request.password:
            raise UserNotFoundError('Invalid password.')

        existing_user.is_logged_in = True
        self.user_storage.update()
        login_response = LoginUserResponse(message="Login successful.")
        return login_response


    def logout(self, logout_request: LogoutUserRequest) -> LogoutUserResponse:
        existing_user = self.user_storage.find_by_username(logout_request.username)
        if existing_user is None:
            raise UserNotFoundError('User not found.')

        existing_user.is_logged_in = False
        self.user_storage.update()
        logout_response = LogoutUserResponse(message="Logout successful.")
        return logout_response