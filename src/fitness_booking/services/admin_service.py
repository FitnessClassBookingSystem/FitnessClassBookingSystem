from fitness_booking.dtos.request.cancel_booking_request import CancelBookingRequest
from fitness_booking.dtos.request.create_session_request import CreateSessionRequest
from fitness_booking.dtos.request.update_session_request import UpdateSessionRequest
from fitness_booking.dtos.response.booking_session_response import BookingSessionResponse
from fitness_booking.dtos.response.cancel_booking_response import CancelBookingResponse
from fitness_booking.dtos.response.create_session_response import CreateSessionResponse
from fitness_booking.dtos.response.update_session_response import UpdateSessionResponse
from fitness_booking.models.booking_model import Booking
from fitness_booking.repositories.mysql_admin_repository import MySQLAdminRepository
from fitness_booking.repositories.mysql_booked_sessions_repository import MySQLBookedSessionRepository
from fitness_booking.repositories.mysql_booking_repository import MySQLBookingRepository


class SessionNotFoundError(Exception):
    pass



class AdminService:

    def __init__(self, instructor_repository: MySQLAdminRepository,
                 booking_repository: MySQLBookingRepository):
        self.instructor_repository = instructor_repository
        self.booking_repository = booking_repository


    def create_session(self, session_request: CreateSessionRequest) -> CreateSessionResponse:
        session = Booking(instructor=session_request.instructor,
                          title=session_request.title,
                          description=session_request.description,
                          session_date=session_request.session_date,
                          start_time=session_request.start_time,
                          end_time=session_request.end_time)

        self.booking_repository.save(session)
        booking_response = CreateSessionResponse(message='session created successfully')
        return booking_response


    def cancel_session(self, cancel_request: CancelBookingRequest) -> CancelBookingResponse:
        existing_booking = (self.booking_repository.find_by_title(cancel_request.session_title))
        if existing_booking is None:
            raise SessionNotFoundError('session not found')

        self.booking_repository.delete_by_title(cancel_request.session_title)
        canceled_session_response = CancelBookingResponse(message='session has been canceled !!!',)
        return canceled_session_response


    def update_session(self, update_request: UpdateSessionRequest) -> UpdateSessionResponse:
        existing_session = (self.booking_repository.find_by_title(update_request.session_title))
        if existing_session is None:
            raise SessionNotFoundError('session not found')

        existing_session.instructor = update_request.new_instructor
        existing_session.title = update_request.new_title
        existing_session.description = update_request.new_description
        existing_session.session_date = update_request.session_date
        existing_session.start_time = update_request.start_time
        existing_session.end_time = update_request.end_time
        self.booking_repository.save(existing_session)
        update_response = UpdateSessionResponse(message='session updated successfully')
        return update_response


    def view_sessions(self) -> list[Booking]:
        return self.booking_repository.find_all()