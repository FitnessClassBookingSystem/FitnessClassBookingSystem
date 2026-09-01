from sqlalchemy.orm import Session

from fitness_booking.models.booking_model import Booking


class MySQLBookedSessionRepository:
    def __init__(self, db: Session):
        self.db = db


    def save(self, booked: Booking) -> Booking:
        self.db.add(booked)
        self.db.commit()
        self.db.refresh(booked)
        return booked


    def delete_by_title(self, title: str) -> None:
        session = self.db.query(Booking).filter(Booking.title == title).first()
        if session:
            self.db.delete(session)
            self.db.commit()


    def find_by_title(self, title: str) -> None | Booking:
        session = self.db.query(Booking).filter(Booking.title == title).first()
        return session


    def find_by_id(self, id: int) -> None | Booking:
        session = self.db.query(Booking).filter(Booking.id == id).first()
        return session


    def find_all(self) -> list[Booking]:
        return self.db.query(Booking).all()


    def delete_all(self) -> None:
        self.db.query(Booking).delete()
        self.db.commit()