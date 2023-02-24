import os
import constants
import tkinter
import customtkinter
import window
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from pathlib import Path

dropdown_var = None
show_images_frame = None
image_frame = None
filenames = []
map = {}

def destroy_frame(frame):
    filenames.remove(map.get(frame))
    map.pop(frame)
    frame.destroy()
    constants.LOADED_IMAGES-=1

def generate_loaded_frames(file):
        image_frame = window.Frame(show_images_frame) 
        image_frame.frame_settings(fg_color='#333333',
                                   wh=[500, 100],
                                   rc=[constants.LOADED_IMAGES, 0],
                                   padxy=[10, 10],
                                   sticky='n')
        image_frame.columnconfigure(2, weight=1)

        map.update({image_frame : file})

        info = os.path.splitext(file)               # Returns location and extension
        name = Path(info[0]).stem  
        
        image_name = customtkinter.CTkLabel(master=image_frame, 
                                            width=100, height=50,
                                            font=customtkinter.CTkFont(family='Uni Sans', size=12),
                                            text=name, 
                                            wraplength=100, 
                                            justify='center')
        image_name.grid(row=0, column=0, padx=20)
        
        delete_button = customtkinter.CTkButton(master=image_frame,
                                                text = constants.STRING_LIST[9], 
                                                font = customtkinter.CTkFont(family='Uni Sans'),
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
                    info = os.path.splitext(filenames[constants.LOADED_IMAGES-1])
                    name = Path(info[0]).stem  
                    Image.open(filenames[constants.LOADED_IMAGES-1]).convert('RGB').save(directory + '/' + name + '.' + dropdown_var.get().lower())
                    
                    destroy_frame(list(map.keys())[list(map.values()).index(filenames[constants.LOADED_IMAGES-1])])
            
            except:
                messagebox.showerror(constants.STRING_LIST[5], constants.STRING_LIST[6])
            
    else:
        messagebox.showerror(constants.STRING_LIST[5], constants.STRING_LIST[7])
