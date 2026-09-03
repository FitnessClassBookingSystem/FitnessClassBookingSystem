from fastapi import APIRouter

from fitness_booking.db.database import SessionLocal
from fitness_booking.dtos.request.booking_session_request import BookingSessionRequest
from fitness_booking.dtos.request.cancel_booking_request import CancelBookingRequest
from fitness_booking.dtos.response.booking_session_response import BookingSessionResponse
from fitness_booking.dtos.response.cancel_booking_response import CancelBookingResponse
from fitness_booking.repositories.mysql_booked_sessions_repository import MySQLBookedSessionRepository
from fitness_booking.repositories.mysql_booking_repository import MySQLBookingRepository
from fitness_booking.repositories.mysql_user_repository import MySQLUserRepository
from fitness_booking.services.user_service import UserService

router = APIRouter()

db = SessionLocal()
user_repository = MySQLUserRepository(db)
booking_repository = MySQLBookingRepository(db)
booked_session_repository = MySQLBookedSessionRepository(db)
user_service = UserService(user_repository, booking_repository, booked_session_repository)


@router.post("/user/book_session", tags=["user"])
def book_session(booking_request: BookingSessionRequest) -> BookingSessionResponse:
    return user_service.book_session(booking_request)

@router.delete("/user/cancel_booking", tags=["user"])
def cancel_booking(cancel_booking_request: CancelBookingRequest) -> CancelBookingResponse:
    return user_service.cancel_booking(cancel_booking_request)