"""This module encompasses functions to allow an enhanced visualization of desired
structures"""
from tkinter import *
from ase.io import write
import threading
import subprocess
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ase.visualize import view
from functools import partial
def run_voila():
    """
    runs in the command line the voila command to view the output of the .jnb file in the folder
    """
    #os.chdir(SCRIPT_DIR)
    notebook_path =SCRIPT_DIR+'\\'+'viewngl.ipynb'
    command = ['voila', notebook_path]
    subprocess.run(command)
def high_res(x):
    """
    renders high definition visualization and enables duplication of structures
    """
    #os.chdir(SCRIPT_DIR)
    write(SCRIPT_DIR+'\\'+'test.vasp',x)
    voila_thread = threading.Thread(target=run_voila)
    voila_thread.start()
def low_res(x):
    """
    renders simplistic visualization and enables saving the structure in desired format (.cif,.vasp ...etc.)
    """
    view(x)
def view_ngl(x):
    """
    creates a window that enables choice between the resolutions available.
    """
    win=Tk()
    win.geometry("50x80")
    b1=Button(win,text="3D",bg="#2A2C2B")
    b1.pack()
    b1['command']=partial(high_res,x)
    b2=Button(win,text="2D",bg="#2A2C2B")
    b2.pack()
    b2['command']=partial(low_res,x)
    b3=Button(win,text="❎",command=win.destroy,fg='red',bg="#2A2C2B")
    b3.pack()
    win.wm_overrideredirect(1)
    win.wm_geometry("+%d+%d" % (500, 500))
    win.configure(background='#555555')
    win.config(highlightbackground="black" ,highlightthickness=1)
    win.mainloop()
