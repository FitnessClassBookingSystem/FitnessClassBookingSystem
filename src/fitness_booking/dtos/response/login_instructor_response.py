from pydantic import BaseModel



class LoginInstructorResponse(BaseModel):
    message: str