from pydantic import BaseModel



class LogoutUserRequest(BaseModel):
    username: str