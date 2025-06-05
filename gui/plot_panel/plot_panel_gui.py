import customtkinter as ctk
from abc import ABC
from .velocity_tab import create_velocity_tab
from .map_tab import create_map_tab
from .stroke_tab import create_stroke_tab
from .compare_tab import create_compare_tab
from .webmap_tab import create_webmap_tab

FONT_TYPE = "Arial"
FONT_SIZE = 12

class PlotPanelGUI(ctk.CTkTabview, ABC):
    CONFIG_FILE = "./conf/config.json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fonts = ctk.CTkFont(family=FONT_TYPE, size=FONT_SIZE, weight="bold")

        self.add("velocity(m/s)")
        self.add("map")
        self.add("stroke")
        self.add("compare")
        self.add("Webmap")

        create_velocity_tab(self)
        create_map_tab(self)
        create_stroke_tab(self)
        create_compare_tab(self)
        create_webmap_tab(self)

        self.texts = []
        self.strokes = []