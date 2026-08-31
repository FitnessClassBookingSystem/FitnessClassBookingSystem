from models.user_model import User
from repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.logged_in_user = None

    def create_user(self, id, name, email, password):
        user = User(id, name, email, password)
        self.user_repository.save(user)
        return user

    def get_user_by_id(self, user_id):
        return self.user_repository.find_by_id(user_id)

    def login(self, email, password):
        user = self.user_repository.find_by_email(email)

        if user and user.password == password:
            self.logged_in_user = user
            return user
        return None

    def logout(self):
        self.logged_in_user = None
        return None
