from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.write()
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from app.common.utils.imports_requiered_pyinstaller import *
from app.modules.moduleHome.home import HomeScreen
from app.modules.moduleSystemSettings.system_settings import SystemSettingsScreen

class App(MDApp):
    def build(self):
        mdscreen_manager = MDScreenManager()
        mdscreen_manager.add_widget(HomeScreen(name="home-screen"))
        mdscreen_manager.add_widget(SystemSettingsScreen(name="system-settings-screen"))
        mdscreen_manager.current = "home-screen"
        return mdscreen_manager