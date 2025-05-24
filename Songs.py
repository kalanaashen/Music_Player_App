from mutagen.mp3 import MP3
import pygame
from mutagen.easyid3 import EasyID3
pygame.mixer.init()
class Songs:
    def __init__(self,audio_path):
        
        self.duration=None
        self.name=None
        self.artist_name=None
        self.audio_path=audio_path
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

            
    def play_music(self):
        try:
            pygame.mixer.music.load(self.audio_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"PLay error  {e}")

    def get_position(self):

        return pygame.mixer.music.get_pos()/1000







        