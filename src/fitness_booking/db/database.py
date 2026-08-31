import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fitness_booking.models.admin_model import Base

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine("mysql+pymysql://root:LUCID1212@localhost/fitness_class_booking_system")
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

class TestAuthService:
    def setup_method(self):
        self.db = SessionLocal()