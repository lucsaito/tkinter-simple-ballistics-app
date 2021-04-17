import ballistics
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    ballistics.MainApplication(root).pack(side = tk.TOP, fill = tk.BOTH, expand = True)
    root.mainloop()
