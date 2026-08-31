from pydantic import BaseModel



class LogoutInstructorRequest(BaseModel):
    username: str