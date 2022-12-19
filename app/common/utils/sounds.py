from gtts import gTTS
import pygame
from pygame import mixer
from playsound import playsound

import os
from helper import getFile
import time
class Sounds:
    language: str = "es"
    def play_audio(self,file_audio: str):
        '''
        carga el video y pasa a repoducirlo
        :param file_audio: ruta del video
        :return:
        '''
        print("play audio")
        playsound(file_audio)
    """
    def play_audio(self,file_audio: str):
        '''
        carga el video y pasa a repoducirlo
        :param file_audio: ruta del video
        :return:
        '''
        print("play audio")
        volumen: float = 1
        mixer.init()
        mixer.music.set_volume(volumen)
        mixer.music.load(file_audio)
        mixer.music.play()
        time.sleep(5)
        mixer.stop()
    """


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