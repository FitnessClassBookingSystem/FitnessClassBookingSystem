from typing import Optional

from pydantic import BaseModel



class RegisterUserResponse(BaseModel):
    message:Optional[str]