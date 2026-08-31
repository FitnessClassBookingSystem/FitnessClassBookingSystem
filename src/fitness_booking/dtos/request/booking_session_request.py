
from pydantic import BaseModel


class BookingSessionRequest(BaseModel):
    session_title: str