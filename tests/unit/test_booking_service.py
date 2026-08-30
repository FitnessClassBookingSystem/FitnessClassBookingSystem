import unittest

from models.booking_model import Booking
from repositories.booking_repository import BookingRepository
from services.booking_service import BookingService


class TestBookingService(unittest.TestCase):

    def test_to_create_booking_service(self):
        repository = BookingRepository()
        service = BookingService(repository)

        booking = service.create_booking(
            1,
            1,
            1,
            "2026-08-30"
        )

        self.assertEqual(booking.id, 1)
        self.assertEqual(booking.student_id, 1)
        self.assertEqual(booking.fitness_class_id, 1)
        self.assertEqual(booking.booking_date, "2026-08-30")

    def test_get_booking_by_id_service(self):
        repository = BookingRepository()
        service = BookingService(repository)

        booking = Booking(
            1,
            1,
            1,
            "2026-08-30"
        )

        repository.save(booking)

        found_booking = service.get_booking_by_id(1)

        self.assertEqual(found_booking, booking)


if __name__ == "__main__":
    unittest.main()