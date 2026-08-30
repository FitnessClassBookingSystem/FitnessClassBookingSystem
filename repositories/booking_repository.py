from models.booking_model import Booking

class BookingRepository:

    def __init__(self):
        self.bookings = []

    def save(self, booking):
        self.bookings.append(booking)

    def find_by_id(self, booking_id):
        for booking in self.bookings:
            if booking.id == booking_id:
                return booking
        return None