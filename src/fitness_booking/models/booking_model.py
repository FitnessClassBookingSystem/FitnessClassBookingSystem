import uuid
from datetime import date, time
from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from fitness_booking.models.admin_model import Base

class Booking(Base):
    __tablename__ = "bookings"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    instructor: Mapped[str] = mapped_column(String(50), nullable=True)
    title: Mapped[str] = mapped_column(String(25), unique=True)
    description: Mapped[str] = mapped_column(String(100))
    session_date: Mapped[date] = mapped_column()
    start_time: Mapped[time] = mapped_column()
    end_time: Mapped[time] = mapped_column()
    booked: Mapped[int] = mapped_column(default=0)