from datetime import datetime, date, time

from pydantic import BaseModel



class UpdateSessionRequest(BaseModel):
    session_title: str
    new_instructor: str
    new_title: str
    new_description: str
    session_date: date
    start_time: time
    end_time: time