from fitness_booking.dtos.request.cancel_booking_request import CancelBookingRequest
from fitness_booking.dtos.response.cancel_booking_response import CancelBookingResponse
from fitness_booking.repositories.mysql_booked_sessions_repository import MySQLBookedSessionRepository
from fitness_booking.repositories.mysql_booking_repository import MySQLBookingRepository
from fitness_booking.repositories.mysql_user_repository import MySQLUserRepository
from fitness_booking.dtos.request.booking_session_request import BookingSessionRequest
from fitness_booking.dtos.response.booking_session_response import BookingSessionResponse
from fitness_booking.services.admin_service import SessionNotFoundError


class UserService:

    def __init__(self, user_storage: MySQLUserRepository,
                 booking_repository: MySQLBookingRepository,
                 booked_session_storage: MySQLBookedSessionRepository):
        self.user_storage = user_storage
        self.booking_repository = booking_repository
        self.booked_session_storage = booked_session_storage


    def book_session(self, booking_request: BookingSessionRequest) -> BookingSessionResponse:
        existing_session = self.booking_repository.find_by_title(booking_request.session_title)
        if existing_session is None:
            raise SessionNotFoundError('session not found')

        new_session = BookingSessionRequest(session_title=booking_request.session_title)
        self.booked_session_storage.save(self.booking_repository.find_by_title(new_session.session_title))
        existing_session.booked +=1
        self.booking_repository.save(existing_session)
        booking_response = BookingSessionResponse(message='you have successfully booked a new session')
        return booking_response


    def cancel_booking(self, cancel_request: CancelBookingRequest) -> CancelBookingResponse:
        existing_booking = (self.booked_session_storage.find_by_title(cancel_request.session_title))
        if existing_booking is None:
            raise SessionNotFoundError('session not found')

        # self.booked_session_storage.delete_by_title(cancel_request.session_title)
        existing_booking.booked -= 1
        self.booked_session_storage.save(existing_booking)
        canceled_session_response = CancelBookingResponse(message='session has been canceled !!!',)
        return canceled_session_response