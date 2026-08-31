from sqlalchemy import Column, String, Integer, UUID
from sqlalchemy.orm import Mapped, mapped_column

from fitness_booking.models.admin_model import Base


class Class(Base):
    __tablename__ = "classes"
    id: Mapped [UUID] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    capacity: Mapped[int] = mapped_column()