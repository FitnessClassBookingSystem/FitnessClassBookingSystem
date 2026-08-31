from fastapi import APIRouter

from repositories.class_repository import ClassRepository
from services.class_service import ClassService

router = APIRouter()

class_repository = ClassRepository()
class_service = ClassService(class_repository)

@router.post("/classes")
def create_class(id: int, title: str, instructor: str, capacity: int):
    return class_service.create_class(id, title, instructor, capacity)

@router.get("/classes")
def get_classes():
    return class_service.get_all_classes()