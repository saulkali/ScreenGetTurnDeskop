import requests
import app.common.constants.api_settings as ApiSettings

from app.common.entities.room_office_display_entity import RoomOfficeDisplayEntity


class RoomApiData:
    def __init__(self):
        pass

    def get_room_office_by_code(self, code: int) -> RoomOfficeDisplayEntity:
        '''
        obtiene el Room Office mediante el codigo de pantalla
        :param code: numero de pantalla
        :return:
        '''
        headers = {'Accept': 'application/json'}
        room_office_display_entity: RoomOfficeDisplayEntity = None
        try:
            http_response = requests.get(
                ApiSettings.host_base + ApiSettings.room_office_by_code + code.__str__(),
                verify=False,
                headers=headers
            )
            if http_response.status_code == 200:
                json_http_response = http_response.json()
                if json_http_response is not None:
                    room_office_display_entity = RoomOfficeDisplayEntity.parse_obj(json_http_response)
        except Exception as error:
            print(error)
        return room_office_display_entity
