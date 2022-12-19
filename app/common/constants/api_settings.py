#host_signal_r = "https://localhost:44393/signalrServer"
host_base = "https://192.168.1.58:5000/"
hub_signal_r = "signalrServer"

#events for websockets
call_turn_endpoint: str = "CallTurn/"
get_turn_endpoint: str = "GetTurns/"

#endpoints api rest
turns_by_room_endpoint: str = "api/SHIFTASSIGNMENT/TurnsByRoom/" #{id_room}
room_office_by_code: str = "api/ROOM/GetRoomOfficeByCode/" #{code}
signage_by_office_endpoint: str = "api/SIGNAGE/GetSignagesPerOffice/" #{id_office}