from typing import List

from sqlalchemy.orm import Session

from fitness_booking.models.class_model import Class


class MySQLClassRepository:

    def __init__(self, db: Session):
        self.db = db


    def save(self, class_: Class):
        self.db.add(class_)
        self.db.commit()
        self.db.refresh(class_)
        return class_


    def find_by_id(self, class_id: Class) -> None | Class:
        class_ = self.db.query(Class).filter(Class.id == class_id.id).one_or_none()
        return class_

    def find_by_title(self, title: str) -> None | Class:
        class_ = self.db.query(Class).filter(Class.title == title).one_or_none()
        return class_

    def find_all(self) -> List[Class]:
        return self.db.query(Class).all()

    def delete(self, class_id: Class) -> None | Class:
        class_ = self.db.query(Class).filter(Class.id == class_id.id).one_or_none()
        self.db.delete(class_)
        self.db.commit()


    def count(self) -> int:
        return self.db.query(Class).count()