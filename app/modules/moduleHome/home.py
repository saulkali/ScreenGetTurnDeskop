import os.path

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy import utils
from kivymd.uix.snackbar import Snackbar

from app.common.utils.sounds import Sounds
from app.common.entities.turn_entity import TurnEntity
from app.common.entities.room_office_display_entity import RoomOfficeDisplayEntity
from app.common.entities.turn_display_entity import TurnDisplayEntity
from app.common.customWidgets.cardWidgetTurn.cardWidgetTurn import CardWidgetTurn
from app.common.customWidgets.cardWidgetTurnInProcess.cardWidgetTurnInProcess import CardWidgetTurnInProcess
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import BoxLayout
from helper import getFile
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from app.common.business.turns_business import TurnsBusiness
from app.common.business.room_business import RoomBusiness
from app.common.business.signage_business import SignageBusiness

from signalrcore.hub_connection_builder import HubConnectionBuilder
import logging
import guid
import app.common.values.integers as integers
from global_system_config import GlobalSystemSettings
from kivy.clock import Clock
from datetime import datetime

Builder.load_file(getFile("app/res/layouts/home.kv"))
class ContentDialogTurnBoxLayout(BoxLayout):
    turn_entity: TurnEntity

    def __init__(self, turn_entity: TurnEntity, *arg, **kwargs):
        super(ContentDialogTurnBoxLayout, self).__init__(*arg, **kwargs)
        self.turn_entity = turn_entity
        self.refresh_label()

    def refresh_label(self):
        if self.turn_entity is not None:
            self.ids.label_title.text = "Turno"
            self.ids.label_name.text = self.turn_entity.turn
            self.ids.label_window.text = self.turn_entity.window
    def set_name_turn(self,name:str):
        self.ids.label_title.text = name

class HomeScreen(MDScreen):
    sounds: Sounds = None
    dialog: MDDialog = None

    room_office_display_entity: RoomOfficeDisplayEntity = None

    list_videos: list[str] = None
    position_video: int = 0
    list_turn_call_await: list[TurnEntity] = []
    turns_business: TurnsBusiness = None
    room_business: RoomBusiness = None
    signage_business: SignageBusiness = None

    hub_connection = HubConnectionBuilder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__setup_global_vars()
        Clock.schedule_once(lambda *args: self.get_id_room(GlobalSystemSettings().system_settings.number_screen))
        Clock.schedule_once(lambda *args: self.__setup_singal_r())
        Clock.schedule_once(lambda *args: self.get_signage())
        Clock.schedule_interval(lambda *args:self.start_clock_time(),1)
        self.__setup_video()


    def start_clock_time(self):
        self.ids.label_clock_time.text = datetime.now().strftime("%d de %b. %Y %I:%M:%S %p")

    def open_system_settings_screen(self):
        self.manager.current = "system-settings-screen"

    def get_list_turns(self, id_room: guid):
        self.turns_business.get_turns(id_room)

    def get_signage(self):
        try:
            self.list_videos = self.signage_business.get_signages(self.room_office_display_entity.idOffice)

            if len(self.list_videos) is not 0:
                self.play_video(GlobalSystemSettings().system_settings.path_files_videos + self.list_videos[self.position_video], True)

        except Exception as error:
            Snackbar(text=f"Error al intentar obtener los videos {error}").open()

    def get_id_room(self, code: int):
        '''
        obtiene el id del room mediante el codigo de la pantalla
        realiza una peticion al servidor que retorna estos datos
        :param code:
        :return:
        '''
        self.room_office_display_entity = self.room_business.get_room_office_by_code(code)
        if self.room_office_display_entity is not None:
            self.ids.top_bar.title = f"Sala: {self.room_office_display_entity.nameRoom} {self.room_office_display_entity.nameOffice}"
            self.turns_business.get_turns(self.room_office_display_entity.idRoom)
            self.__set_turns_display()

    def __set_turns_display(self):
        '''
        agrega los datos a la pantalla, turnos y los turnos en proceso
        realiza la peticion de los turnos y los pinta en un MDList y en
        un recycleView
        :return:
        '''
        self.ids.recycle_view_turns.data = []
        self.ids.recycle_view_turns_in_process.data = []

        turn_display_entity: TurnDisplayEntity = self.turns_business.get_turns(self.room_office_display_entity.idRoom)
        if turn_display_entity is not None:
            for turn in (turn_display_entity.waitingTurns1 + turn_display_entity.waitingTurns2):
                self.ids.recycle_view_turns.data.append({
                    "name": turn.turn
                })
            if turn_display_entity.actualTurn is not None:
                self.ids.recycle_view_turns_in_process.data.append({
                    "name": turn_display_entity.actualTurn.turn,
                    "window": turn_display_entity.actualTurn.window,
                    "color_card": utils.get_color_from_hex("#772582"),
                    "text_color_general": utils.get_color_from_hex("#FFFFFF")
                })
            if turn_display_entity.recentTurn is not None:
                self.ids.recycle_view_turns_in_process.data.append({
                    "name":turn_display_entity.recentTurn.turn,
                    "window": turn_display_entity.recentTurn.window,
                    "color_card": utils.get_color_from_hex("#FFFFFF"),
                    "text_color_general": utils.get_color_from_hex("#000000")
                })

    def on_call_turn(self,data):
        '''
        genera el evento del websocket que se encarga de llamar el turno
        en la pantalla
        :param args:
        :return:
        '''
        if type(data) == list:
            turn_entity: TurnEntity = TurnEntity.parse_obj(data[0])
            if turn_entity is not None:
                Clock.schedule_once(
                    lambda *args: self.show_dialog_turn(f"turno { (turn_entity.turn[0:1] + ' ' + turn_entity.turn[1:len(turn_entity.turn)])} {turn_entity.window}",
                                                        turn_entity))
                Clock.schedule_once(lambda *args: self.get_id_room(GlobalSystemSettings().system_settings.number_screen))

    def on_get_turn(self,*args):
        '''
        genera el evento del web socket que obtiene un turno nuevo
        viene en conjunto del kiosko cuando toma un turno este
        evento se dispara
        :param args:
        :return:
        '''
        Clock.schedule_once(lambda *args: self.get_id_room(GlobalSystemSettings().system_settings.number_screen))

    def __setup_singal_r(self):
        '''
        configura el websockets para iniciar su conexion con el servidor
        :return:
        '''
        try:
            print("connect websocket")
            self.hub_connection = HubConnectionBuilder() \
                .with_url(
                    GlobalSystemSettings().api_settings.host_base + GlobalSystemSettings().api_settings.hub_signal_r,
                    options={
                    "verify_ssl": False
                    }
                ) \
                .with_automatic_reconnect({
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 5
                }).build()

            self.hub_connection.on_open(
                lambda: print("connection opened and handshake received ready to send messages"))
            self.hub_connection.on_close(lambda: print("connection closed"))
            self.hub_connection.on_error(lambda data: print(f"An exception was thrown closed{data.error}"))

            self.hub_connection.on(
                GlobalSystemSettings().api_settings.call_turn_endpoint + self.room_office_display_entity.idRoom.__str__(),
                callback_function=self.on_call_turn
            )
            self.hub_connection.on(
                GlobalSystemSettings().api_settings.get_turn_endpoint + self.room_office_display_entity.idRoom.__str__(),
                callback_function=self.on_get_turn
            )
            self.hub_connection.start()
            print("signal connected :)")
        except Exception as error:
            Snackbar(text=str(error)).open()

    def __setup_global_vars(self):
        '''
        Configura las variables globales de la propia clase
        :return:
        '''
        self.sounds = Sounds()
        self.turns_business = TurnsBusiness()
        self.room_business = RoomBusiness()
        self.signage_business = SignageBusiness()

    def __setup_video(self):
        '''
        configura propiedades del reproductor de video
        :return:
        '''
        self.ids.video.bind(eos=lambda *args: self.__next_video(*args))

    def __next_video(self, instance, value):
        '''
        evento que se dispara al finalizar el video y carga el siguiente video
        :param instance:
        :param value:
        :return:
        '''
        self.position_video += 1
        if self.position_video > len(self.list_videos):
            self.position_video = 0

        self.play_video(GlobalSystemSettings().system_settings.path_files_videos + self.list_videos[self.position_video], True)


    def close_dialog_turn(self, turn_entity: TurnEntity):
        '''
        cierra el dialogo, o en otras palabras cierra el modal
        :param args:
        :return:
        '''
        if self.dialog is not None:
            self.dialog.dismiss()
            self.dialog = None
            self.resumen_video()
            self.show_video()
            if len(self.list_turn_call_await) is not 0:
                print(f"======= {len(self.list_turn_call_await)} =========")
                next_turn_entity: TurnEntity = self.list_turn_call_await.pop(0)
                Clock.schedule_once(
                    lambda *args: self.show_dialog_turn(f"turno {next_turn_entity.turn} {next_turn_entity.window}",
                                                        next_turn_entity))
                Clock.schedule_once(
                    lambda *args: self.get_id_room(GlobalSystemSettings().system_settings.number_screen))
    def hiden_video(self):
        '''
        oculta el video
        :return:
        '''
        self.ids.video.opacity = 0.1

    def show_video(self):
        '''
        muestra el video
        :return:
        '''
        self.ids.video.opacity = 1

    def pause_video(self):
        '''
        pausa el video
        :return:
        '''
        self.ids.video.state = "pause"

    def resumen_video(self):
        '''
        renuda el video
        :return:
        '''
        self.ids.video.state = "play"

    def show_dialog_turn(self, message: str, turn_entity: TurnEntity):
        '''
        muestra el turno que sigue mediante un modal (MDDialog)
        :param message: mensaje que sera mostrado en el modal
        :return:
        '''
        self.pause_video()
        self.hiden_video()
        content_dialog_turn: ContentDialogTurnBoxLayout = ContentDialogTurnBoxLayout(turn_entity)
        self.list_turn_call_await.append(turn_entity)
        if self.dialog is None:
            self.dialog = MDDialog(
                type="custom",
                content_cls=content_dialog_turn
            )
            self.dialog.open()
            Clock.schedule_once(lambda *args: self.sounds.text_to_speatch(message))
            Clock.schedule_once(callback= lambda *args: self.close_dialog_turn(self.list_turn_call_await.pop(0)), timeout=integers.interval_time_dialog)
    def add_item_recycleview(self, turn_entity: TurnEntity):
        '''
        agrega los items al recycle view
        :param turn_entity: entidad del turno que sera agregado al recycleView
        :return:
        '''
        self.ids.recycle_view_turns.data.append({
            "turn_entity": turn_entity
        })

    def play_video(self, path_video: str, player_local: bool):
        '''
        reproduce el video que se le indique, tanto locales como del servidor
        :param path_video: url del video
        :param player_local: indica que si al reproducir videos sea local o desde el servidor
        :return:
        '''
        try:
            if os.path.exists(path_video):
                if player_local is True:
                    self.ids.video.source = getFile(path_video)
                else:
                    self.ids.video.source = path_video
                self.resumen_video()
            else:
                self.__next_video(None,None)

        except Exception as error:
            Snackbar(text=f"Error al reproducir video: {error}").open()
