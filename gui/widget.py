import json
import os.path

import customtkinter
from typing import Union, Callable
from PIL import Image, ImageTk
from tkinter import filedialog

class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            if value < 0.0:
                value = 0.0

            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))


class IconButton(customtkinter.CTkButton):
    def __init__(self,master,icon_path,text,command=None,size=(48,48),**kwargs):
        """
        汎用的なアイコンボタンのクラス
        Args:
            master: 親ウィジェット
            icon_paht: アイコン画像のパス
            command:ボタンクリック時に呼び出される関数
            size:アイコン画像のサイズ
            **kwargs: 追加オプション
        """
        
        icon_image = Image.open(icon_path).resize(size)
        self.icon_photo = customtkinter.CTkImage(light_image=icon_image,dark_image=icon_image)


        super().__init__(
            master,
            image=self.icon_photo,
            text=text,
            text_color="black",
            command=command,
            fg_color="transparent",
            hover_color="lightgray",
            **kwargs,
        )

class ConfigWindow(customtkinter.CTkToplevel):
    CONFIG_FILE = "./conf/config.json"
    DEFAULT_CONFIG = {
        "reference_file_path":"",
        "mode":"UT"
    }

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("300x300")
        self.title("Config window")
        config_frame = customtkinter.CTkFrame(self)
        config_frame.pack(fill="both", expand=True, padx=5, pady=5)
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))

        self.current_config = self.load_config

        def select_file():
            file_path = filedialog.askopenfilename(
                title="トップ選手のデータを選んでください",
                filetypes=[("Stroke Files", "*.stroke"),
                           ("JSON Files", "*.json"),
                           ("All Files", "*.*")]
            )
            if file_path:
                print(file_path)
                self.current_config["reference_file_path"] = file_path

        file_button = customtkinter.CTkButton(
            config_frame,
            text="Select File",
            command=select_file
        )
        file_button.pack(pady=20)

        mode_label = customtkinter.CTkLabel(config_frame, text="mode Select")
        mode_var = customtkinter.StringVar(value="UT")
        modes = ["UT", "RR"]
        mode_dropdown = customtkinter.CTkOptionMenu(
            config_frame,
            values=modes,
            variable=mode_var
        )
        mode_dropdown.pack(pady=10)

        def confirm_selection():
            self.current_config["mode"] = mode_var.get()
            self.save_config(self.current_config)
            print(f"mode:{mode_var.get()}")

        confirm_button = customtkinter.CTkButton(
            config_frame,
            text="Save",
            command=confirm_selection
        )
        confirm_button.pack(pady=20)

    def load_config(self):
        if os.path.exists(self.CONFIG_FILE):
            self.save_config(self.DEFAULT_CONFIG)
            return self.DEFAULT_CONFIG
        with open(self.CONFIG_FILE,"r") as f:
            return json.load(f)

    def save_config(self, config):
        os.makedirs(os.path.dirname(self.CONFIG_FILE),exist_ok=True)
        with open(self.CONFIG_FILE, 'w') as f:
            json.dump(config,f,indent=4)

if __name__ == "__main__":
    app = customtkinter.CTk()

    spinbox_1 = FloatSpinbox(app, width=150, step_size=10)
    spinbox_1.pack(padx=20, pady=20)


    spinbox_1.set(35)
    print(spinbox_1.get())

    app.mainloop()