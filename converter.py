import os
import constants
import customtkinter
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from pathlib import Path

global dropdown_var
global show_images_frame
global filenames
global  image_frame
filenames = []
map = {}

def destroy_frame(frame):
    filenames.remove(map.get(frame))
    map.pop(frame)
    frame.destroy()
    constants.LOADED_IMAGES-=1

def generate_loaded_frames(file):
        image_frame = customtkinter.CTkFrame(master=show_images_frame, fg_color="gray", width=500, height=100)
        image_frame.grid(row=constants.LOADED_IMAGES, padx=10, pady=10, sticky='n')
        image_frame.grid_propagate(False)
        image_frame.columnconfigure(2, weight=1)

        map.update({image_frame : file})

        loc, ext = os.path.splitext(file)
        name = Path(loc).stem  
        
        image_name = customtkinter.CTkLabel(master=image_frame, width=100, height=50, text=name, wraplength=100, justify="center")
        image_name.grid(row=0, column=0, padx=20)

        delete_button = customtkinter.CTkButton(master=image_frame, 
                                                command=lambda frame=image_frame: destroy_frame(frame))
        delete_button.grid(row=0, column=2, padx=10, pady=(35, 35), sticky='e')

        constants.LOADED_IMAGES+=1
    
def selectDirectory():
    global directory
    directory = filedialog.askdirectory()

def loadFiles():
    loaded_files = filedialog.askopenfilenames(filetypes=constants.IMAGETYPES)
    for file in loaded_files:
        try:
            filenames.index(file)
        except:
            filenames.append(file)
            generate_loaded_frames(file)

def startConversion():
    if dropdown_var.get() != constants.STRING_LIST[2]:
            if len(filenames) == 0:
                messagebox.showerror(constants.STRING_LIST[5], constants.STRING_LIST[8])
                return
            try:
                while len(filenames) != 0:
                    loc, ext = os.path.splitext(filenames[constants.LOADED_IMAGES-1])
                    name = Path(loc).stem  
                    Image.open(filenames[constants.LOADED_IMAGES-1]).convert('RGB').save(directory + "/" + name + '.' + dropdown_var.get().lower())
                    
                    key_list = list(map.keys())
                    val_list = list(map.values())
                    pos = val_list.index(filenames[constants.LOADED_IMAGES-1])
                    destroy_frame(key_list[pos])
            
            except:
                messagebox.showerror(constants.STRING_LIST[5], constants.STRING_LIST[6])
            
    else:
        messagebox.showerror(constants.STRING_LIST[5], constants.STRING_LIST[7])