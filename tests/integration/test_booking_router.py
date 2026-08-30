import unittest

from fastapi.testclient import TestClient
from main import app


class TestBookingRouter(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_to_create_booking(self):
        response = self.client.post(
            "/booking",
            params={
                "id": 1,
                "student_id": 1,
                "fitness_class_id": 1,
                "booking_date": "2026-08-30"
            })
        self.assertEqual(response.status_code, 200)

    def test_to_get_booking(self):
        self.client.post(
            "/bookings",
            params={
                "id": 1,
                "student_id": 1,
                "fitness_class_id": 1,
                "booking_date": "2026-08-30"
            }
        )
        response = self.client.get("/bookings/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["id"], 1)
        self.assertEqual(data["student_id"], 1)
        self.assertEqual(data["fitness_class_id"], 1)
        self.assertEqual(data["booking_date"], "2026-08-30")


if __name__ == '__main__':
    unittest.main()
