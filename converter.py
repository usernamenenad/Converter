import os
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from pathlib import Path
import constants

global dropdown_var

IMAGETYPES = [(constants.STRING_LIST[4], "*.jpg"), (constants.STRING_LIST[4], "*.png")]

def selectDirectory():
    global directory
    directory = filedialog.askdirectory()

def loadFiles():
    global filenames
    filenames = filedialog.askopenfilenames(filetypes=IMAGETYPES)
    
def startConversion():
    if dropdown_var.get() != constants.STRING_LIST[2]:
        try:
            for file in filenames:
                loc, ext = os.path.splitext(file)
                name = Path(loc).stem  
                Image.open(file).convert('RGB').save(directory + "/" + name + '.' + dropdown_var.get().lower())

        except:
            messagebox.showerror(constants.STRING_LIST[5], constants.STRING_LIST[6])
            
    else:
        messagebox.showerror(constants.STRING_LIST[5], constants.STRING_LIST[7])