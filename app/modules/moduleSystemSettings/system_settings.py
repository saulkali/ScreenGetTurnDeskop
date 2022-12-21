from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from kivy.lang import Builder
from helper import getFile
from global_system_config import GlobalSystemSettings

if GlobalSystemSettings().system_settings.is_windows():
    import os
    import win32com.shell.shell as shell


Builder.load_file(getFile("app/res/layouts/systemSettings.kv"))


class SystemSettingsScreen(MDScreen):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.__global_settings_system()

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
        '''
            crea el acceso directo para ejecutarse al iniciar windows
        '''
        wDir = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
        path = os.path.join(wDir, "main.lnk")
        if not os.path.exists(path):
            target = getFile("main.exe")
            program_for_execute = "wscript"
            file_vbs_create_shurtcut = getFile("staticfiles/utilsWindows/ShortCut.vbs")
            commands = f'{file_vbs_create_shurtcut} "{target}" "{path}"'
            shell.ShellExecuteEx(
                lpVerb='runas',
                lpFile=program_for_execute,
                lpParameters=commands)

    def create_auto_launch_linux(self):
        pass

    def create_auto_launch(self):
        try:
            if self.ids.mdcp_launch_automatic.active:
                if GlobalSystemSettings().system_settings.is_unix():
                    self.create_auto_launch_linux()
                elif GlobalSystemSettings().system_settings.is_windows():
                    self.create_auto_launch_in_windows()
                else:
                    print("error sistema operativo desconocido")
        except Exception as error:
            print(error)
