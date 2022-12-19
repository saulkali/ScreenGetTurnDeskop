import guid
from app.common.apiData.turns_api_data import TurnsApiData
from app.common.entities.turn_display_entity import TurnDisplayEntity

class TurnsBusiness:
    turns_api_data: TurnsApiData = None

    def __init__(self):
        self.turns_api_data = TurnsApiData()

    def get_turns(self, id_room: guid) -> TurnDisplayEntity:
        return self.turns_api_data.get_turns(id_room)

