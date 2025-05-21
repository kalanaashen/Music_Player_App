from typing import Tuple
import customtkinter as ctk
from PIL import Image


ctk.set_appearance_mode("Dark")




class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Music Player")
        self.geometry("500x750")
        self.load_widgets()
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1) 
        self.columnconfigure(2,weight=1) 

    def load_widgets(self):

        music_logo=Image.open("music.png")
        play_logo=Image.open('play.png')
        next_song=ctk.CTkImage(light_image=Image.open("next.png"),dark_image=Image.open("next.png"),size=(30,30))
        previuos_song=ctk.CTkImage(light_image=Image.open("back.png"),dark_image=Image.open("back.png"),size=(30,30))
        play_logo_png=ctk.CTkImage(light_image=play_logo,dark_image=play_logo,size=(50,50))
        music_logo_png=ctk.CTkImage(light_image=music_logo,dark_image=music_logo,size=(150,150))
        self.play_logo_label=ctk.CTkButton(self,image=play_logo_png,text="",fg_color="SpringGreen2",command=None,hover_color="SpringGreen3",width=20)
        self.music_logo_label=ctk.CTkLabel(self,image=music_logo_png,text="",)
        self.previuos_song_button=ctk.CTkButton(self,image=previuos_song,text="",width=12,fg_color="SpringGreen2",command=None,hover_color="SpringGreen3")
        self.next_song_button=ctk.CTkButton(self,image=next_song,text="",width=12,fg_color="SpringGreen2",command=None,hover_color="SpringGreen3")
        self.browse_song=ctk.CTkButton(self,text="Browse Files")
        self.next_song_button.grid(row=1,column=2)
        self.play_logo_label.grid(row=1,column=1)
        self.music_logo_label.grid(row=0,column=0,columnspan=3)
        #self.browse_song.grid(row=0,column=1)
        self.previuos_song_button.grid(row=1,column=0)
app=App()
app.mainloop()













    