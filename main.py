from fastapi import FastAPI

from fitness_booking.routers import admin_router, auth_router
from fitness_booking.routers.auth_router import router as class_router
from fitness_booking.routers.admin_router import router as admin_router
from fitness_booking.routers.user_router import router as user_router

app = FastAPI()
app.include_router(class_router)
app.include_router(admin_router)
app.include_router(user_router)