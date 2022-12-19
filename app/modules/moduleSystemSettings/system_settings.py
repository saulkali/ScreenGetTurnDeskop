from kivymd.uix.screen import MDScreen

class SystemSettingsScreen(MDScreen):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

    def open_home_screen(self):
        self.manager.current = "home-screen"