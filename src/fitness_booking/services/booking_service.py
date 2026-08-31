from fitness_booking.dtos.request.booking_session_request import BookingSessionRequest
from fitness_booking.dtos.request.cancel_booking_request import CancelBookingRequest
from fitness_booking.dtos.request.create_session_request import CreateSessionRequest
from fitness_booking.dtos.request.update_session_request import UpdateSessionRequest
from fitness_booking.dtos.response.booking_session_response import BookingSessionResponse
from fitness_booking.dtos.response.cancel_booking_response import CancelBookingResponse
from fitness_booking.dtos.response.create_session_response import CreateSessionResponse
from fitness_booking.dtos.response.update_session_response import UpdateSessionResponse
from fitness_booking.models.booking_model import Booking
from fitness_booking.repositories.mysql_booked_sessions_repository import MySQLBookedSessionRepository
from fitness_booking.repositories.mysql_booking_repository import MySQLBookingRepository


class SessionNotFoundError(Exception):
    pass

class BookingServices:

    def __init__(self, booking_repository: MySQLBookingRepository,
                 booked_sessions_repository: MySQLBookedSessionRepository):
        self.booking_repository = booking_repository
        self.booked_sessions_repository = booked_sessions_repository


    def create_session(self, session_request: CreateSessionRequest) -> CreateSessionResponse:
        session = Booking(title=session_request.title,
                          date=session_request.date,
                          start_time=session_request.start_time,
                          end_time=session_request.end_time)
        self.booking_repository.save(session)
        booking_response = CreateSessionResponse(message='session created successfully',
                                             date=session_request.date)
        return booking_response


    def book_session(self, booking_request: BookingSessionRequest) -> BookingSessionResponse:
        existing_session = self.booking_repository.find_by_title(booking_request.title)
        if existing_session == None:
            raise SessionNotFoundError('session not found')

        new_session = BookingSessionRequest(session_title=booking_request.session_title)
        self.booked_sessions_repository.save(new_session)
        booking_response = BookingSessionResponse(message='you have successfully booked a new session',)
        return booking_response


    def cancel_session(self, cancel_request: CancelBookingRequest) -> CancelBookingResponse:
        existing_booking = (self.booked_sessions_repository.find_session_by_title(cancel_request.session_title))
        if existing_booking == None:
            raise SessionNotFoundError('session not found')

        self.booked_sessions_repository.delete_session_by_title(cancel_request.title)
        canceled_session_response = CancelBookingResponse(message='session has been canceled !!!',)
        return canceled_session_response


    def update_session(self, update_request: UpdateSessionRequest) -> UpdateSessionResponse:
        existing_session = (self.booking_repository.find_by_title(update_request.session_title))
        if existing_session == None:
            raise SessionNotFoundError('session not found')

        existing_session.title = update_request.new_title
        existing_session.date = update_request.date
        existing_session.start_time = update_request.start_time
        existing_session.end_time = update_request.end_time
        update_response = UpdateSessionResponse(message='session updated successfully')
        return update_response