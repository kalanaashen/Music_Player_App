from typing import Tuple
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
from Songs import *
from custombox import CustomMessageBox

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
        self.path_label=None
        self.total=None
        self.is_playing=False
        self.is_pause=False

    def load_widgets(self):

        music_logo=Image.open("music.png")
        pause_logo=Image.open('pause.png')
        play_logo=Image.open('play.png')
        self.progress_bar=ctk.CTkProgressBar(self,orientation="horizontal",width=200,height=10,progress_color="SpringGreen2")
        self.progress_bar.set(0)
        self.song_details=ctk.CTkLabel(self,text="")


        self.pause_png=ctk.CTkImage(light_image=pause_logo,dark_image=pause_logo,size=(30,30))
        next_song=ctk.CTkImage(light_image=Image.open("next.png"),dark_image=Image.open("next.png"),size=(30,30))
        previuos_song=ctk.CTkImage(light_image=Image.open("back.png"),dark_image=Image.open("back.png"),size=(30,30))
        self.play_logo_png=ctk.CTkImage(light_image=play_logo,dark_image=play_logo,size=(50,50))
        music_logo_png=ctk.CTkImage(light_image=music_logo,dark_image=music_logo,size=(150,150))

        self.play_logo_label=ctk.CTkButton(self,image=self.play_logo_png,text="",fg_color="SpringGreen2",hover_color="SpringGreen3",width=20,command=self.play_music_button)
        self.music_logo_label=ctk.CTkLabel(self,image=music_logo_png,text="",)
        self.previuos_song_button=ctk.CTkButton(self,image=previuos_song,text="",width=12,fg_color="SpringGreen2",command=None,hover_color="SpringGreen3")
        self.next_song_button=ctk.CTkButton(self,image=next_song,text="",width=12,fg_color="SpringGreen2",command=None,hover_color="SpringGreen3")
        self.browse_song=ctk.CTkButton(self,text="Browse Files",command=self.browse_files)
        self.song_details.grid(row=0,column=1,sticky='nsew')
        self.next_song_button.grid(row=3,column=2)
        self.play_logo_label.grid(row=3,column=1)
        self.music_logo_label.grid(row=1,column=0,columnspan=3)
        self.browse_song.grid(row=1,column=2,sticky='e')
        self.progress_bar.grid(row=2,column=0,columnspan=3,sticky="nsew")
        self.previuos_song_button.grid(row=3,column=0)

    def browse_files(self):

        file_path=filedialog.askopenfilename(title="Open your music File",filetypes=[("MP3 files","*.mp3"),("All files","*.*")])
        self.path_label=file_path
        self.song=Songs(file_path)
        song_name=self.song.name
        song_artist=self.song.artist_name
        self.duration=self.song.duration
        self.song_details.configure(self,text=f"{song_name}\n {song_artist}",font=("Arial",16,"bold"))

    def update_progress(self):

        if self.path_label:

            current=self.song.get_position()  
            total=self.duration
            progress = min(current / total, 1.0)
            self.progress_bar.set(progress)
        self.after(500,self.update_progress)
    
    def play_music_button(self):
        
        try:
            if not self.is_playing:
                self.song.play_music()
                self.play_logo_label.configure(image=self.pause_png)
                self.update_progress()
                self.is_playing = True
                self.is_paused = False
            elif self.is_playing and not self.is_paused:
                self.song.pause_music()
                self.play_logo_label.configure(image=self.play_png)
                self.is_paused = True
            elif self.is_playing and self.is_paused:
                self.song.resume_music()
                self.play_logo_label.configure(image=self.pause_png)
                self.is_paused = False
        except:

            cus=CustomMessageBox(self,"NOTICE","Please Select a Song!")
            

app=App()
app.mainloop()













