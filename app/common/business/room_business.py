from app.common.entities.room_office_display_entity import RoomOfficeDisplayEntity
from app.common.apiData.room_api_data import RoomApiData

class RoomBusiness:
    room_api_data:RoomApiData = None
    def __init__(self):
        self.room_api_data = RoomApiData()
    def get_room_office_by_code(self,code:int) -> RoomOfficeDisplayEntity:
        return self.room_api_data.get_room_office_by_code(code)