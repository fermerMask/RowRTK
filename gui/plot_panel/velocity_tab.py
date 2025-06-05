from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import customtkinter as ctk

class VelocityTab:
    def __init__(self, master):
        self.fig, self.ax = plt.subplots()
        self. velocitycanvas = FigureCanvasTkAgg(self.fig, master=master)
        self.velocitycanvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)
        self.ax.set_title("Velocity Graph")
    
    def velocity_plot(self, ts, vs):
        self.ax.cla()
        self.ax.plot(ts, vs, label="Velocity (m/s)", color='blue')
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Velocity (m/s)")
        self.ax.grid(True)
        self.ax.legend()
        self.velocitycanvas.draw()
    