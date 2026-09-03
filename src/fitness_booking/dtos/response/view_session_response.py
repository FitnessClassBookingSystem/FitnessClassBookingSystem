from datetime import date, time
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ViewSessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    instructor: str
    title: str
    description: str
    session_date: date
    start_time: time
    end_time: time
    booked: int