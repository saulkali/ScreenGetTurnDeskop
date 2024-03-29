
class ApiSettings:
    host_base = "https://192.168.1.58:5000/"
    hub_signal_r = "signalrServer"

    #events for websockets
    call_turn_hub_reference: str = "CallTurn/"
    get_turn_hub_reference: str = "GetTurns/"

    #endpoints api rest
    turns_by_room_endpoint: str = "api/SHIFTASSIGNMENT/TurnsByRoom/" #{id_room}
    room_office_by_code: str = "api/ROOM/GetRoomOfficeByCode/" #{code}
    signage_by_office_endpoint: str = "api/SIGNAGE/GetSignagesPerOffice/" #{id_office}