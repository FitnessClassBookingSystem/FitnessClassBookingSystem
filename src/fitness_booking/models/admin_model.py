import uuid
from uuid import UUID


from sqlalchemy import String
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass

class Admin(Base):
    __tablename__ = "admins"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(15), unique=True)
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(15))
    is_logged_in: Mapped[bool] = mapped_column(default=False)