import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from .utils import nmea, Stroke

class StrokeTab:
    def __init__(self, master, acc_speed_switch, stroke_index_label):
        self.fig, (self.ax_speed, self.ax_accel) = plt.subplots(2, 1, figsize=(6, 4))
        self.strokecanvas = FigureCanvasTkAgg(self.fig, master=master)
        self.strokecanvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.acc_speed_switch = acc_speed_switch
        self.stroke_index_label = stroke_index_label

        self.strokes = []
        self.current_stroke_index = 0

    def stroke_plot(self, t1, t2, tw):
        self.ax_speed.cla()
        self.ax_accel.cla()

        try:
            self.vs, ts = nmea.get_vels(t1, t2)
            strokes, mean_period, num = Stroke.extract_strokes(self.vs, ts, tw)

            if not strokes or mean_period == 0 or num == 0:
                messagebox.showerror("ERROR", "有効なストロークが検出されませんでした")
                return

            self.strokes = strokes
            self.current_stroke_index = 0
            self.show_stroke_by_index(self.current_stroke_index)
            self.update_stroke_index_label()

        except Exception as e:
            messagebox.showerror("ERROR", f"ストロークプロットに失敗しました: {e}")

    def show_stroke_by_index(self, index):
        if not self.strokes or index < 0 or index >= len(self.strokes):
            return

        self.ax_speed.cla()
        self.ax_accel.cla()

        vel, time = self.strokes[index]
        rel_time = [t - time[0] for t in time]
        self.ax_speed.plot(rel_time, nmea.filter_gnss_noise(vel), "b-", label="velocity(m/s)")

        if self.acc_speed_switch.get() == "on":
            acc = np.gradient(nmea.filter_gnss_noise(vel), rel_time)
            self.ax_accel.plot(rel_time, acc, "r--", label="acceleration(m/s^2)")
            self.ax_accel.set_ylabel("Acceleration(m/s^2)")
            self.ax_accel.tick_params(axis="y")

        self.ax_speed.set_xlabel("Time(s)")
        self.ax_speed.set_ylabel("Boat Speed(m/s)")
        self.ax_speed.grid(":")
        self.ax_speed.legend()
        self.strokecanvas.draw()

    def show_prev_stroke(self):
        if self.current_stroke_index > 0:
            self.current_stroke_index -= 1
            self.show_stroke_by_index(self.current_stroke_index)
            self.update_stroke_index_label()

    def show_next_stroke(self):
        if self.current_stroke_index < len(self.strokes) - 1:
            self.current_stroke_index += 1
            self.show_stroke_by_index(self.current_stroke_index)
            self.update_stroke_index_label()

    def update_stroke_index_label(self):
        if self.stroke_index_label:
            self.stroke_index_label.configure(
                text=f"{self.current_stroke_index+1}/{len(self.strokes)}"
            )
