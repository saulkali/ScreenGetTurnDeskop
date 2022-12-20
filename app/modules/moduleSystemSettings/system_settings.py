from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from kivy.lang import Builder
from helper import getFile
from global_system_config import GlobalSystemSettings

import app.common.values.strings as Strings

if GlobalSystemSettings().system_settings.type_os == Strings.type_os_windows :
    import os,winshell
    from win32com.client import Dispatch


Builder.load_file(getFile("app/res/layouts/systemSettings.kv"))
class SystemSettingsScreen(MDScreen):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.__global_settings_system()

        self.ids.mdcp_launch_automatic.active = True

    def __global_settings_system(self):
        self.ids.text_field_number_screen.text = GlobalSystemSettings().system_settings.number_screen.__str__()
        self.ids.text_field_url_api.text = GlobalSystemSettings().api_settings.host_base.__str__()
        self.ids.mdcp_update_automatic.active = GlobalSystemSettings().system_settings.active_automatic_updates
    def open_home_screen(self):
        self.manager.current = "home-screen"

    def save_settings(self):
        GlobalSystemSettings().system_settings.number_screen = int(self.ids.text_field_number_screen.text)
        GlobalSystemSettings().api_settings.host_base = self.ids.text_field_url_api.text
        GlobalSystemSettings().save()

        self.open_home_screen()
        Snackbar(text="Los ajustes se guardaron de manera correcta").open()
    def create_auto_launch_in_windows(self):
        desktop = winshell.desktop()
        path = os.path.join(desktop, "Media Player Classic.lnk")
        target = r"P:\Media\Media Player Classic\mplayerc.exe"
        wDir = r"P:\Media\Media Player Classic"
        icon = r"P:\Media\Media Player Classic\mplayerc.exe"
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()

    def create_auto_launch_linux(self):
        pass

    def create_auto_launch(self):
        try:
            if GlobalSystemSettings().system_settings.type_os in Strings.type_os_unix:
                pass
            elif GlobalSystemSettings().system_settings.type_os is Strings.type_os_windows:
                self.create_auto_launch_in_windows()
            else:
                print("error sistema operativo desconocido")
        except Exception as error:
            print(error)
