from pydantic import BaseModel



class CancelBookingRequest(BaseModel):
    session_title: str