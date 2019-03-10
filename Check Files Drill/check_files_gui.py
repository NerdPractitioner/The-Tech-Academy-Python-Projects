#
# -*- coding: utf-8 -*-
#
# Python Ver:   3.7.2
#
# Author:       Daniel A. Christie
#
# Purpose:      Tkinter check files drill from The Tech Academy
#               
#
# Tested OS:  This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

import check_files_main
import check_files_func

def load_gui(self):
    self.btn_browse1 = tk.Button(self.master,width=12,height=1, text='Browse...')
    self.btn_browse1.grid(row=0, column=0, padx=(10,0), pady=(30,0),sticky=N+W)

    self.btn_browse2 = tk.Button(self.master,width=12,height=1, text='Browse...')
    self.btn_browse2.grid(row=1, column=0, padx=(10,0), pady=(5,0),sticky=N+W)

    self.btn_check_files = tk.Button(self.master,width=12,height=2, text='Check for files...')
    self.btn_check_files.grid(row=2, column=0, padx=(10,0), pady=(5,0),sticky=W)

    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: check_files_func.ask_quit(self))
    self.btn_close.grid(row=2,column=2,padx=(10,40),pady=(5,0), sticky=E)

    #Entry fields
    self.txt_browse1 = tk.Entry(self.master, width=50, text='')
    self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=2,padx=(10,40),pady=(30,0), sticky=W+E)

    self.txt_browse2 = tk.Entry(self.master, width=50,  text='')
    self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=2,padx=(10,40),pady=(5,0), sticky=W+E)

    
    
    







if __name__ == "__main__":
    pass
