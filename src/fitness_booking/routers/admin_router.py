from fastapi import APIRouter

from fitness_booking.db.database import SessionLocal
from fitness_booking.dtos.request.cancel_booking_request import CancelBookingRequest
from fitness_booking.dtos.request.create_session_request import CreateSessionRequest
from fitness_booking.dtos.request.update_session_request import UpdateSessionRequest
from fitness_booking.dtos.response.cancel_booking_response import CancelBookingResponse
from fitness_booking.dtos.response.create_session_response import CreateSessionResponse
from fitness_booking.dtos.response.update_session_response import UpdateSessionResponse
from fitness_booking.repositories.mysql_booking_repository import MySQLBookingRepository
from fitness_booking.repositories.mysql_user_repository import MySQLUserRepository
from fitness_booking.services.admin_service import AdminService

router = APIRouter()

db = SessionLocal()
user_repository = MySQLUserRepository(db)
booking_repository = MySQLBookingRepository(db)
admin_service = AdminService(user_repository, booking_repository)

@router.post("/admin/create_session", tags=["admin"])
def create_session(session_request: CreateSessionRequest) -> CreateSessionResponse:
    return admin_service.create_session(session_request)

@router.post("/admin/cancel_session", tags=["admin"])
def cancel_session(session_request: CancelBookingRequest) -> CancelBookingResponse:
    return admin_service.cancel_session(session_request)

@router.post("/admin/update", tags=["admin"])
def update_session(session_request: UpdateSessionRequest) -> UpdateSessionResponse:
    return admin_service.update_session(session_request)