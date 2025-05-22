from mutagen.mp3 import MP3
import pygame
from mutagen.easyid3 import EasyID3

class Songs:
    def __init__(self):
        
        self.duration=None
        self.name=None
        self.artist_name=None
        self.audio_path="Kanda Pirimeda.mp3"
        self.find_name()
        self.find_length()
        self.find_artist()


    def find_name(self):
        try:
            audio=EasyID3(self.audio_path)
            self.name=audio.get("title", ["Unknown Title"])[0]
        except Exception as e:
            print("Length error",e)
             

    def find_length(self):
        try:
            audio=MP3("Kanda Pirimeda.mp3")
            length=(audio.info.length)
            self.duration=length
        except Exception as e:
            print("Length error",e)

    def find_artist(self):
        try:
            audio=EasyID3(self.audio_path)
            self.artist_name=audio.get("artist", ["Unknown Artist"])[0]
        except Exception as e:
            print("artist name error",e)






song=Songs()




        