import unittest

from models.user_model import User
from repositories.user_repository import UserRepository
from services.user_service import UserService


class TestUserService(unittest.TestCase):

    def test_to_create_user_service(self):
        repository = UserRepository()
        service = UserService(repository)

        user = service.create_user(
            1,
            "Sharon Lucy",
            "sharon@gmail.com",
            "1234"
        )

        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Sharon Lucy")
        self.assertEqual(user.email, "sharon@gmail.com")
        self.assertEqual(user.password, "1234")

    def test_to_get_user_by_id_service(self):
        repository = UserRepository()
        service = UserService(repository)

        user = User(
            1,
            "Sharon Lucy",
            "sharon@gmail.com",
            "1234"
        )

        repository.save(user)

        found_user = service.get_user_by_id(1)

        self.assertEqual(found_user, user)

    def test_to_find_user_by_email(self):
        repository = UserRepository()

        user = User(
            1,
            "Sharon Lucy",
            "sharon@gmail.com",
            "1234"
        )
        repository.save(user)
        found_user = repository.find_by_email("sharon@gmail.com")

        self.assertEqual(found_user, user)

    def test_to_login_user(self):
        repository = UserRepository()
        service = UserService(repository)

        user = User(
            1,
            "Sharon Lucy",
            "sharon@gmail.com",
            "1234"
        )
        repository.save(user)

        found_user = service.login(
            "sharon@gmail.com",
            "1234"
        )
        self.assertEqual(found_user, user)

    def test_to_login_user_with_wrong_password(self):
        repository = UserRepository()
        service = UserService(repository)

        user = User(
            1,
            "Sharon Lucy",
            "sharon@gmail.com",
            "1234"
        )
        repository.save(user)

        found_user = service.login(
            "sharon@gmail.com",
            "lucy1234"
        )
        self.assertEqual(found_user, None)

    def test_to_logout_user(self):
        repository = UserRepository()
        service = UserService(repository)

        user = User(
            1,
            "Sharon Lucy",
            "sharon@gmail.com",
            "1234"
        )
        repository.save(user)

        service.login(
            "sharon@gmail.com",
            "1234"
        )
        service.logout()
        self.assertEqual(service.logged_in_user, None)


if __name__ == "__main__":
    unittest.main()