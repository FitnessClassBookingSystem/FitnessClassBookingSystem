import unittest

from fastapi.testclient import TestClient
from main import app


class TestUserRouter(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_to_create_user(self):
        response = self.client.post(
            "/users", params={
                "id": 1,
                "name": "Sharon Lucy",
                "email": "sharon@gmail.com",
                "password": "1234"
            })
        self.assertEqual(response.status_code,200)

    def test_to_get_user(self):
        self.client.post(
            "/users", params={
                "id": 1,
                "name": "Sharon Lucy",
                "email": "sharon@gmail.com",
                "password": "1234"
            })
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code,200)

        data = response.json()

        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "Sharon Lucy")
        self.assertEqual(data["email"], "sharon@gmail.com")

    def test_to_login_user(self):
        response = self.client.post(
            "/login",
            params={
                "email": "sharon@gmail.com",
                "password": "1234"
            }
        )
        self.assertEqual(response.status_code,200)

    def test_to_login_user_with_unknown_email(self):
        response = self.client.post(
            "/login",
            params={
                "email": "lucy_jkl@gmail.com",
                "password": "1234"
            }
        )
        self.assertEqual(response.status_code,200)


    def test_to_logout_user(self):
        response = self.client.post("/logout")

        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()
