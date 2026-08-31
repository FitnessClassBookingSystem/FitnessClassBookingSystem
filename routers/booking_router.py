from fastapi import APIRouter

from repositories.booking_repository import BookingRepository
from services.booking_service import BookingService

router = APIRouter()

booking_repository = BookingRepository()
booking_service = BookingService(booking_repository)

@router.post("/bookings")
def create_booking(
        id: int,
        student_id: int,
        fitness_class_id: int,
        booking_date: str
):
    return booking_service.create_booking(
        id,
        student_id,
        fitness_class_id,
        booking_date
    )
@router.get("/bookings/{booking_id}")
def get_booking(booking_id: int):
    return booking_service.get_booking_by_id(booking_id)