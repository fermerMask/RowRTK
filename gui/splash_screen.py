import customtkinter as ctk
import time

class SplashScreen(ctk.CTkToplevel):
    def __init__(self, master, width=400, height=200, title="Loading...", progress_message="Initializing..."):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.title_text = title
        self.progress_message = progress_message

        # スプラッシュスクリーンの初期設定
        self.geometry(f"{self.width}x{self.height}+500+300")
        self.overrideredirect(True)
        self.resizable(False, False)

        # UIの構築
        self.init_ui()

    def init_ui(self):
        splash_frame = ctk.CTkFrame(self)
        splash_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.label = ctk.CTkLabel(splash_frame, text=self.title_text, font=("meirio", 18))
        self.label.pack(pady=20)

        self.progress_bar = ctk.CTkProgressBar(splash_frame, orientation="horizontal", mode="determinate")
        self.progress_bar.pack(pady=20, padx=20)
        self.progress_bar.set(0)

    def update_progress(self, value, message=None):
        self.progress_bar.set(value)
        if message:
            self.label.configure(text=message)
        self.update_idletasks()

    def close(self):
        self.destroy()



