from kivy.properties import ObjectProperty,StringProperty
from kivymd.uix.card import MDCard
from app.common.entities.turn_entity import TurnEntity



class CardWidgetTurn(MDCard):
    name: TurnEntity = ObjectProperty(None)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)