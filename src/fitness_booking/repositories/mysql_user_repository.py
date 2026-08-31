from typing import List

from uuid import UUID
from sqlalchemy.orm import Session

from fitness_booking.models.user_model import User


class MySQLUserRepository:

    def __init__(self, db: Session):
        self.db = db


    def save(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user


    def update(self) -> None:
        self.db.commit()


    def delete_by_username(self, username: str) -> None:
        user = (self.db.query(User).filter(User.username == username).first())
        if user:
            self.db.delete(user)
            self.db.commit()


    def find_by_username(self, username: str) -> User | None:
        user = (self.db.query(User).filter(User.username == username).one_or_none())
        return user


    def find_by_id(self, user_id: UUID) -> User | None:
        user = (self.db.query(User).filter(User.id == user_id).one_or_none())
        return user


    def find_by_email(self, email: str) -> User | None:
        user = (self.db.query(User).filter(User.email == email).one_or_none())
        return user


    def find_all(self) -> List[User]:
        return self.db.query(User).all()


    def delete_all(self) -> None:
        self.db.query(User).delete()
        self.db.commit()

    def count(self) -> int:
        return self.db.query(User).count()