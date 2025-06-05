import os
import sys

from tkinter import filedialog,messagebox
import tkinter as tk

import matplotlib.pyplot as plt
from .pll_rtk_lib import NMEA

nmea = NMEA()

class GraphDrawer:
    def avg_vel(vs,ts):
        minutes = []
        vel_avg = []
        count = 0
        for i in range(0, len(vs), 300):
            s_vel = sum(vs[i:i+300]) / 300
            count += 1
            vel_avg.append(s_vel)
            minutes.append(count)
        return vel_avg,minutes,ts[-1]/60

    def time_to_second(time_str):
        minutes, seconds = time_str.split(":")
        minutes = int(minutes)
        seconds = int(seconds)
        total_seconds = minutes * 60 + seconds 
        return total_seconds

    def change(avg_v):
        distance = 500
        time_str = []
        for v in avg_v:
            if v <= 1.0:
                minute = 10
                second = 10
            else:
                time = distance / v
                minute = int(time/ 60)
                second = int(time % 60)
                
            t = f"{minute}:{second:02d}"
            time_str.append(t)
        
        return time_str


class FuncClass:
    def __init__(self) -> None:
        pass
    
    def file_read(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = filedialog.askopenfilename(filetypes=[("TXT,NMEA","*.txt;*.nmea")],initialdir=current_dir)

        if len(file_path) != 0:
            return file_path
        else:
            messagebox.showinfo("情報","ファイルが選択されていません")
            return None
        
    def file_load(self,file_name):
        file_path = self.file_read()
        if file_path is not None and len(file_path) != 0:
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            file_name.delete(0,tk.END)
            file_name.insert(0,base_name)
            messagebox.showinfo("情報","Data loading...")
            nmea.load(file_path)



if __name__ == "__main__":
    file = "../data/rtk-watanabe2.txt"
    nmea = NMEA()
    nmea.load(file)

    xs, ys, zs, vs, modes, ts, _, _ = nmea.get_3d()

    avg_v, min_S, min2 = GraphDrawer.avg_vel(vs,ts)

    time_data = GraphDrawer.change(avg_v)
    time_data = [GraphDrawer.time_to_second(t) for t in time_data]
    x_data = range(0, len(time_data))
    average = sum(time_data) / len(time_data)
    plt.plot(x_data,time_data,marker="o")
    plt.gca().invert_yaxis()

    yticks = [min(time_data),max(time_data),int(average)]
    yticks_label = [f"{t // 60}:{t % 60:02d}" for t in yticks]

    plt.yticks(yticks, yticks_label)
    plt.xlabel("minutes")
    plt.ylabel("time (/500m)") 
    plt.show()    


import os
import sys

from tkinter import filedialog,messagebox
import tkinter as tk

import matplotlib.pyplot as plt
from lib.pll_rtk_lib import NMEA

nmea = NMEA()

class GraphDrawer:
    def avg_vel(vs,ts):
        minutes = []
        vel_avg = []
        count = 0
        for i in range(0, len(vs), 300):
            s_vel = sum(vs[i:i+300]) / 300
            count += 1
            vel_avg.append(s_vel)
            minutes.append(count)
        return vel_avg,minutes,ts[-1]/60

    def time_to_second(time_str):
        minutes, seconds = time_str.split(":")
        minutes = int(minutes)
        seconds = int(seconds)
        total_seconds = minutes * 60 + seconds 
        return total_seconds

    def change(avg_v):
        distance = 500
        time_str = []
        for v in avg_v:
            if v <= 1.0:
                minute = 10
                second = 10
            else:
                time = distance / v
                minute = int(time/ 60)
                second = int(time % 60)
                
            t = f"{minute}:{second:02d}"
            time_str.append(t)
        
        return time_str


class FuncClass:
    def __init__(self) -> None:
        pass
    
    def file_read(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = filedialog.askopenfilename(filetypes=[("TXT,NMEA","*.txt;*.nmea")],initialdir=current_dir)

        if len(file_path) != 0:
            return file_path
        else:
            messagebox.showinfo("情報","ファイルが選択されていません")
            return None
        
    def file_load(self,file_name):
        file_path = self.file_read()
        if file_path is not None and len(file_path) != 0:
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            file_name.delete(0,tk.END)
            file_name.insert(0,base_name)
            messagebox.showinfo("情報","Data loading...")
            nmea.load(file_path)



if __name__ == "__main__":
    file = "../data/rtk-watanabe2.txt"
    nmea = NMEA()
    nmea.load(file)

    xs, ys, zs, vs, modes, ts, _, _ = nmea.get_3d()

    avg_v, min_S, min2 = GraphDrawer.avg_vel(vs,ts)

    time_data = GraphDrawer.change(avg_v)
    time_data = [GraphDrawer.time_to_second(t) for t in time_data]
    x_data = range(0, len(time_data))
    average = sum(time_data) / len(time_data)
    plt.plot(x_data,time_data,marker="o")
    plt.gca().invert_yaxis()

    yticks = [min(time_data),max(time_data),int(average)]
    yticks_label = [f"{t // 60}:{t % 60:02d}" for t in yticks]

    plt.yticks(yticks, yticks_label)
    plt.xlabel("minutes")
    plt.ylabel("time (/500m)") 
    plt.show()    


