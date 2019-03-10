from tkinter import *
import tkinter as tk


import check_files_gui
import check_files_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(450,150)
        self.master.maxsize(450,150)
        check_files_func.center_window(self,450,150)
        self.master.title("Check Files Drill")
        self.master.configure(bg='#F0F0F0')
        self.master.protocol("WM_DELETE_WINDOW", lambda: check_files_func.ask_quit(self))
        arg = self.master

        check_files_gui.load_gui(self)


if __name__ == "__main__":
    #creates window with tkinter
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
