import unittest

from fastapi.testclient import TestClient

from main import app


class TestClassRouter(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_to_create_class(self):
        response = self.client.post(
            "/classes",
            params={
                "id": 1,
                "title": "Morning Yoga",
                "instructor": "Fitness Master",
                "capacity": 20
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_to_get_all_classes(self):
        self.client.post(
            "/classes",
            params={
                "id": 1,
                "title": "Morning Yoga",
                "instructor": "Fitness Master",
                "capacity": 20
            }
        )

        response = self.client.get("/classes")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertTrue(len(data) > 0)


if __name__ == "__main__":
    unittest.main()