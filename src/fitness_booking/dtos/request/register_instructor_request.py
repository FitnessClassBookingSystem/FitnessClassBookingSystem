from pydantic import BaseModel, Field


class RegisterInstructorRequest(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str
    password: str = Field(min_length=6, max_length=15)