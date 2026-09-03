from pydantic import BaseModel



class BookingSessionRequest(BaseModel):
    username: str
    session_title: str