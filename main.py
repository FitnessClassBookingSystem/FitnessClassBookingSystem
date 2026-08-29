from fastapi import FastAPI

from routers.user_router import  router as user_router
from routers.class_router import router as class_router

app = FastAPI()
app.include_router(user_router)
app.include_router(class_router)
