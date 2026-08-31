from pydantic import BaseModel



class CancelBookingResponse(BaseModel):
    message: str