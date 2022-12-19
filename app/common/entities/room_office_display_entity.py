from uuid import uuid4,UUID
from pydantic import BaseModel,Field

class RoomOfficeDisplayEntity(BaseModel):
    idOffice:UUID = Field(default_factory=uuid4)
    idRoom:UUID = Field(default_factory=uuid4)
    nameOffice:str
    nameRoom:str
    sound:int
    timeMessage:int
