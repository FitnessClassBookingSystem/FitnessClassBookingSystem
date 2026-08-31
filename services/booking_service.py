from models.booking_model import Booking
from repositories.booking_repository import BookingRepository


class BookingService:

    def __init__(self, booking_repository):
        self.booking_repository = booking_repository

    def create_booking(self, id, student_id, fitness_class_id, booking_date):
        booking = Booking(
            id,
            student_id,
            fitness_class_id,
            booking_date
        )

        self.booking_repository.save(booking)

        return booking

    def get_booking_by_id(self, booking_id):
        return self.booking_repository.find_by_id(booking_id)