# from fastapi import APIRouter
#
# from fitness_booking.repositories.mysql_admin_repository import MySQLAdminRepository
# from fitness_booking.repositories.mysql_booking_repository import MySQLBookingRepository
# from fitness_booking.services.booking_service import BookingServices
# from services_test.test_admin_service import SessionLocal
#
# router = APIRouter()
#
# db = SessionLocal()
# booking_repository = MySQLBookingRepository(db)
# admin_repository = MySQLAdminRepository(db)
# booking_service = BookingServices(admin_repository, booking_repository)