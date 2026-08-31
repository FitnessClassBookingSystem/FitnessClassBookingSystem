from pydantic import BaseModel



class CreateSessionResponse(BaseModel):
    date: date
    message: str