import unittest
from models.booking_model import Booking
from repositories.booking_repository import BookingRepository



class TestBookingRepository(unittest.TestCase):

    def test_to_save_booking(self):
        repository = BookingRepository()

        booking = Booking(
            1,
            1,
            1,
            "2026-08-30"
        )
        repository.save(booking)

        self.assertIn(booking, repository.bookings)

    def test_to_find_booking_by_id(self):
        repository = BookingRepository()

        booking = Booking(
            1,
            1,
            1,
            "2026-08-30"
        )
        repository.save(booking)

        found_booking = repository.find_by_id(1)

        self.assertEqual(found_booking, booking)


if __name__ == '__main__':
    unittest.main()
