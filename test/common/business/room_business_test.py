import unittest
from app.common.business.room_business import RoomBusiness
from app.common.entities.room_office_display_entity import RoomOfficeDisplayEntity


class RoomBusinessTest(unittest.TestCase):
    room_business:RoomBusiness

    def setUp(self) -> None:
        self.room_business = RoomBusiness()

    def test_get_room_office_by_code_null(self):
        room_office_display_entity: RoomOfficeDisplayEntity = self.room_business.get_room_office_by_code(3)
        self.assertIsNone(room_office_display_entity)