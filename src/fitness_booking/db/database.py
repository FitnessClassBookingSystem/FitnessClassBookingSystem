import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fitness_booking.models.admin_model import Base
from fitness_booking.models.booking_model import Booking
from fitness_booking.models.user_model import User

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine("mysql+pymysql://root:LUCID1212@localhost/fitness_class_booking_system")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)