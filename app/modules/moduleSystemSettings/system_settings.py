from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from helper import getFile
from global_system_config import GlobalSystemSettings

Builder.load_file(getFile("app/res/layouts/systemSettings.kv"))
class SystemSettingsScreen(MDScreen):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.__global_settings_system()

    def __global_settings_system(self):
        self.ids.text_field_number_screen.text = GlobalSystemSettings().system_settings.number_screen.__str__()
        self.ids.text_field_url_api.text = GlobalSystemSettings().api_settings.host_base.__str__()
    def open_home_screen(self):
        self.manager.current = "home-screen"

    def save_settings(self):
        GlobalSystemSettings().save()