from kivy.properties import StringProperty,ColorProperty
from kivymd.uix.card import MDCard

class CardWidgetTurnInProcess(MDCard):
    name: str  = StringProperty()
    window: str = StringProperty()
    color_card = ColorProperty()
    text_color_general = ColorProperty()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)