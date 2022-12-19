from gtts import gTTS
from pygame import mixer
from playsound import playsound
from global_system_config import GlobalSystemSettings
import os
from helper import getFile

import time
class Sounds:
    language: str = "es"
    def play_audio(self,file_audio: str):
        '''
        carga el audio y pasa a repoducirlo
        :param file_audio: ruta del video
        :return:
        '''
        print("play audio")
        if GlobalSystemSettings().system_settings.type_os in ["Darwin","Linux"]:
            self.play_audio_in_unix(file_audio)
        elif GlobalSystemSettings().system_settings.type_os is "Windows":
            self.play_audio_in_windows(file_audio)
        else:
            print("no se pudo reproducir el audio plataforma desconocida")
    def play_audio_in_unix(self,file_audio: str):
        volumen: float = 1
        mixer.init()
        mixer.music.set_volume(volumen)
        mixer.music.load(file_audio)
        mixer.music.play()

    def play_audio_in_windows(self,file_audio: str):
        playsound(file_audio)

    def text_to_speatch(self,message:str):
        '''
        a partir de un texto lo convierte en audio para despues, reproducirlo
        :param message: menssage que sera transformado en audio
        :return:
        '''
        file_audio_name: str = "speach.mp3"
        audio = gTTS(text=message,lang=self.language,slow=False)
        if os.path.isfile(getFile(file_audio_name)):
            os.remove(getFile(file_audio_name))
        audio.save(file_audio_name)
        self.play_audio(file_audio_name)