import os
import geopandas as gp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from utils.path import get_resource_path

class MapTab:
    def __init__(self, master):
        self.fig, self.ax = plt.subplots()
        self.mapcanvas = FigureCanvasTkAgg(self.fig, master=master)
        self.mapcanvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def map_plot(self, xs, ys, vs, place):
        self.ax.cla()

        if place == 'toda':
            path = get_resource_path('place/toda')
            rdedg = gp.read_file(os.path.join(path, '20221001-rdedg.shp'))
        elif place == 'ojima':
            path = get_resource_path('place/ojima')
            rdedg = gp.read_file(os.path.join(path, '20240401-rdedg.shp'))
        elif place == 'nagano':
            path = get_resource_path('place/nagano')
            rdedg = gp.read_file(os.path.join(path, '20240401-rdedg.shp'))
        else:
            return

        rdedg.plot(ax=self.ax, color='gray', zorder=4)

        vmax = max(vs)
        self.ax.scatter(xs, ys, marker='o', s=4, c=vs, cmap='jet', vmin=0.0, vmax=vmax, zorder=5)
        self.ax.set_xlim(min(xs)-50, max(xs)+50)
        self.ax.set_ylim(min(ys)-50, max(ys)+50)
        self.mapcanvas.draw()
