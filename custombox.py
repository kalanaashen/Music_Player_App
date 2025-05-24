import customtkinter as ctk


class CustomMessageBox(ctk.CTkToplevel):
    def __init__(self, parent, title="Alert", message="alert"):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x150")
        self.resizable(False, False)
        self.grab_set()  

        self.label = ctk.CTkLabel(self, text=message, wraplength=250, justify="center",font=("verdana",12,"bold"))
        self.label.pack(pady=20, padx=10)

        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok,fg_color="spring green",hover_color="light sea green")
        self.ok_button.pack(pady=10)

    def on_ok(self):
        self.destroy()
