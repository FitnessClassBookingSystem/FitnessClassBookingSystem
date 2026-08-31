from datetime import date as Date, time as Time

from pydantic import BaseModel, Field


class CreateSessionRequest(BaseModel):
    title: str = Field(max_length=25)
    instructor: str = Field(max_length=50)
    session_date: Date = Field(...)
    start_time: Time = Field(...)
    end_time: Time = Field(...)