import tkinter as tk
from tkinter import ttk
import math

w_height = 200
w_width = 500

def center_window(frame):  #Takes a tk.Frame as input and return its centralized geomtry
    window_height = int(frame.winfo_screenheight() * 0.3)
    window_width = int(frame.winfo_screenwidth() * 0.3)
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int(
        (screen_height / 2) - (window_height / 2))
    geometry = "{}x{}+{}+{}".format(w_width, w_height, x_cordinate, y_cordinate)
    return geometry

def calculate_time(frame):

    g = 9.8
    velocity = float(frame.velocityEntry.get())
    angle = float(frame.angleEntry.get()) * 0.0174533
    height = float(frame.heightEntry.get())

    y_vel = float(velocity) * math.sin(angle)
    eq1 = 4*(y_vel**2) + 8*g*height     #gt^2 -2vot - 2height = 0
    delta = math.sqrt(eq1)
    tempo = (2*y_vel + delta)/(2*g)

    frame.time.config(text="{} s".format(str(tempo)))

def config_main_layout(frame):
    frame.velocityLabel.grid(row=1, column=0, sticky=tk.W)
    frame.velocityEntry.grid(row=1, column=1)
    frame.angleLabel.grid(row=2, column=0, sticky=tk.W)
    frame.angleEntry.grid(row=2, column=1)
    frame.heightLabel.grid(row=3, column=0, sticky=tk.W)
    frame.heightEntry.grid(row=3, column=1)

    frame.timeoffallLabel.grid(row=4, column=0, sticky=tk.W)
    frame.time.grid(row=4, column=1, sticky=tk.W)
    frame.calculate.grid(row=5, column=2, sticky=tk.E)



class Main(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.title = tk.Label(self, text="Properties:")
        self.title.grid(row = 0, column = 0, sticky = tk.W)

        self.velocityLabel = tk.Label(self, text="Initial velocity:")
        self.angleLabel = tk.Label(self, text="Angle of velocity vector(degrees):")
        self.heightLabel = tk.Label(self, text="Initial height:")
        self.timeoffallLabel = tk.Label(self, text="Time of fall:")

        self.time = tk.Label(self, text = "")
        self.calculate = tk.Button(self, text="Calculate", command =lambda : calculate_time(self))

        self.velocityEntry = tk.Entry(self)
        self.angleEntry = tk.Entry(self)
        self.heightEntry = tk.Entry(self)
        self.layout = config_main_layout(self)

class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.resizable(False, False)


        self.master.title("Ballistics=")
        self.master.geometry(center_window(self))

        self.title = tk.Label(self, text="Falling time of a projectile.")
        self.title.pack()
        self.MainFrame = Main(self).pack(side = tk.TOP, fill = tk.BOTH, expand = True)



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side = tk.TOP, fill = tk.BOTH, expand = True)
    root.mainloop()
