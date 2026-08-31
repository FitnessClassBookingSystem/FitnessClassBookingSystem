from uuid import UUID

from sqlalchemy.orm import Session

from fitness_booking.models.booking_model import Booking


class MySQLBookingRepository:
    def __init__(self, db: Session):
        self.db = db


    def save(self, booking: Booking) -> Booking:
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking


    def delete_by_title(self, title: str) -> None:
        session = self.db.query(Booking).filter(Booking.title == title).first()
        if session:
            self.db.delete(session)
            self.db.commit()


    def find_by_title(self, title: str) -> None | Booking:
        session = self.db.query(Booking).filter(Booking.title == title).first()
        return session


    def find_by_id(self, booking_id: UUID) -> Booking | None:
        session = self.db.query(Booking).filter(Booking.id == booking_id).first()
        return session

    def delete_by_id(self, booking_id: UUID) -> None:
        session = self.db.query(Booking).filter(Booking.id == booking_id).first()
        if session:
            self.db.delete(session)
            self.db.commit()


    def find_all(self) -> list[Booking]:
        return self.db.query(Booking).all()


    def delete_all(self) -> None:
        self.db.query(Booking).delete()
        self.db.commit()


    def count(self) -> int:
        return self.db.query(Booking).count()

    # def update(self) -> None:
    #     session = self.db.query(Booking).filter(Booking_id)