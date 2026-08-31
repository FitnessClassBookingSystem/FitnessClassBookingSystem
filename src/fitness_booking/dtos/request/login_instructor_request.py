from pydantic import BaseModel



class LoginInstructorRequest(BaseModel):
    username: str
    email: str