import guid
import requests
import pydantic

from app.common.entities.turn_display_entity import TurnDisplayEntity
import app.common.constants.api_settings as ApiSettings

class TurnsApiData:

    def __init__(self):
        pass

    def get_turns(self, id_room: guid) -> TurnDisplayEntity:
        '''
        obtiene los turnos en espera y lo que se encuentran atendidos
        :param id_room: id de la sala
        :return:
        '''
        list_turns: TurnDisplayEntity = None
        print("obteniendo los turnos")
        try:
            http_response = requests.get(
                ApiSettings.host_base + ApiSettings.turns_by_room_endpoint + id_room.__str__(),
                verify= False
            )
            if http_response.status_code == 200:
                json_list_turns = http_response.json()
                print(json_list_turns)
                if json_list_turns is not None:
                    list_turns = TurnDisplayEntity.parse_obj(json_list_turns)
        except Exception as error:
            print(error)
        return list_turns
