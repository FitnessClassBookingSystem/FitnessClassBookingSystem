from pydantic import BaseModel, Field



class RegisterUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=15)
    email: str = Field(...)
    password: str = Field(min_length=6, max_length=15)