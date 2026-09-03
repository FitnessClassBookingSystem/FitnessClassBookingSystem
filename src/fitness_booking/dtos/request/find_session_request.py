from pydantic import BaseModel



class FindSessionRequest(BaseModel):
    session_id: str