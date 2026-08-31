from fastapi import APIRouter

from repositories.user_repository import UserRepository
from services.user_service import UserService

router = APIRouter()

user_repository = UserRepository()
user_service = UserService(user_repository)

@router.post("/users")
def create_user(id: int, name: str, email: str, password: str):
    return user_service.create_user(id, name, email, password)

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return user_service.get_user_by_id(user_id)

@router.post("/login")
def login(email: str, password: str):
    return user_service.login(email, password)

@router.post("/logout")
def logout_user():
    return user_service.logout()