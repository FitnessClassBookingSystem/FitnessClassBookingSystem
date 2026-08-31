from datetime import datetime, date

from pydantic import BaseModel



class UpdateSessionRequest(BaseModel):
    new_title: str
    new_instructor: str
    session_date: date
    start_time: datetime
    end_time: datetime