from kivy.properties import StringProperty
from kivymd.uix.card import MDCard

class CardWidgetTurnInProcess(MDCard):
    name: str  = StringProperty()
    window: str = StringProperty()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)