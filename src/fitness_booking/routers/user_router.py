from fastapi import APIRouter

from fitness_booking.db.database import SessionLocal
from fitness_booking.dtos.request.login_user_request import LoginUserRequest
from fitness_booking.dtos.request.logout_user_request import LogoutUserRequest
from fitness_booking.dtos.request.register_user_request import RegisterUserRequest
from fitness_booking.dtos.response.login_user_response import LoginUserResponse
from fitness_booking.dtos.response.logout_user_response import LogoutUserResponse
from fitness_booking.dtos.response.register_user_response import RegisterUserResponse
from fitness_booking.repositories.mysql_user_repository import MySQLUserRepository
from fitness_booking.services.auth_service import AuthService

router = APIRouter()

db = SessionLocal()
user_repository = MySQLUserRepository(db)
auth_service = AuthService(user_repository)


# @router.post("/auth")
#
# class UserRouter(APIRouter):

@router.post("/auth/register")
def register(self, register_request: RegisterUserRequest) -> RegisterUserResponse:
    return auth_service.register(register_request)

@router.post("/auth/login")
def login(self, login_request: LoginUserRequest) -> LoginUserResponse:
    return auth_service.login(login_request)

@router.post("/auth/logout")
def logout(self, logout_request: LogoutUserRequest) -> LogoutUserResponse:
    return auth_service.logout(logout_request)