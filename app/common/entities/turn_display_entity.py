from .turn_entity import TurnEntity
from pydantic import BaseModel


class TurnDisplayEntity(BaseModel):
    actualTurn: TurnEntity = None
    recentTurn: TurnEntity = None
    waitingTurns1: list[TurnEntity] = []
    waitingTurns2: list[TurnEntity] = []
