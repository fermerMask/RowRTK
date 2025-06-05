import customtkinter as ctk
from tkinter import messagebox
import sys
#from gui.plot_panel.plot_panel_gui import PlotPanelGUI
#from gui.control_panel.control_panel_gui import ControlPanelGUI
#from utils import get_resource_path, close_all, updater
from config import APP_NAME, APP_VERSION, FONT_TYPE, FONT_SIZE
#import nmea

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        #self.iconbitmap(default=get_resource_path('assets') + r"\rowrtk_icon.ico")
        self.title(APP_NAME + APP_VERSION)
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)

        '''
        self.check_for_updates()

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.plot_frame = PlotPanelGUI(self)
        self.plot_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.data_frame = ControlPanelGUI(self)
        self.data_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    def check_for_updates(self):
        updater.check_for_updates()

    def on_closing(self):
        if messagebox.askyesno(title="終了確認", message="アプリケーションを終了しますか？"):
            close_all()
            self.destroy()
            sys.exit()

    def update(self, start_time, end_time, tw, place):
        if (start_time == 0) and (end_time == 0):
            xs, ys, zs, vs, modes, ts, theta, distance = nmea.get_3d()
        else:
            xs, ys, zs, vs, modes, ts, theta, distance = nmea.get_3d(start_time, end_time)
            self.plot_frame.stroke_plot(start_time, end_time, tw)

        messagebox.showinfo("情報", "Data loaded")
        self.plot_frame.vel_plot(ts, vs)
        self.plot_frame.map_plot(xs, ys, vs, place)
        self.data_frame.dash_board_data(ts, vs, distance)
        self.data_frame.detail_data(ts, vs)

    '''
