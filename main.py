from fastapi import FastAPI

from fitness_booking.routers.user_router import router as class_router

app = FastAPI()
app.include_router(class_router)