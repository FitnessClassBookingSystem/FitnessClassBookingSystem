import unittest
from models.booking_model import Booking

class TestBooking(unittest.TestCase):

    def test_to_create_booking(self):
        booking = Booking(
            1,
            1,
            1,
            "2026-08-30"
        )
        self.assertEqual(booking.id, 1)
        self.assertEqual(booking.student_id, 1)
        self.assertEqual(booking.fitness_class_id, 1)
        self.assertEqual(booking.booking_date, "2026-08-30")


if __name__ == '__main__':
    unittest.main()
