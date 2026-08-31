import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fitness_booking.dtos.request.create_session_request import CreateSessionRequest
from fitness_booking.dtos.request.login_user_request import LoginUserRequest
from fitness_booking.dtos.request.register_user_request import RegisterUserRequest
from fitness_booking.models.admin_model import Base, Admin
from fitness_booking.repositories.mysql_booking_repository import MySQLBookingRepository
from fitness_booking.repositories.mysql_user_repository import MySQLUserRepository
from fitness_booking.services.admin_service import AdminService
from fitness_booking.services.auth_service import AuthService

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine("mysql+pymysql://root:LUCID1212@localhost/fitness_class_booking_system")
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

class TestAdminService:
    def setup_method(self):
        self.db = SessionLocal()
        self.user_repository = MySQLUserRepository(self.db)
        self.booking_repository = MySQLBookingRepository(self.db)

            # self.register = AuthService(self.user_repository)
            #
            # register_request = RegisterUserRequest(username="lucid", email="sharon@gmail.com", password="password")
            # self.register.register(register_request)
            # login_request = LoginUserRequest(username="lucid", password="password")
            # self.register.login(login_request)
            #
            # self.album = PlaylistService(self.playlist_repository, self.register.current_user)


    def test_adminCanCreate_session(self):
        process = AdminService(self.user_repository, self.booking_repository)
        create_request = CreateSessionRequest(title='acl', session_date='2026-10-07', start_time='15:00', end_time='20:00')
        response = process.create_session(create_request)
        assert response.date == '2026-3-04'