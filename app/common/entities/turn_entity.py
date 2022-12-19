from uuid import uuid4,UUID
from pydantic import BaseModel,Field

from datetime import datetime

class TurnEntity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    turn: str = ""
    window: str = ""
    appointment: bool = False
    date:datetime = datetime.now()