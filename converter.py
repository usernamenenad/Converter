import tkinter
import customtkinter
import os
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from pathlib import Path

STRING_1 = "Choose files"
STRING_2 = "Start conversion"
STRING_3 = "Select conversion type"
STRING_4 = "Select destination folder"
STRING_5 = "Images"
STRING_6 = "Error!"
STRING_7 = "Conversion error! Check if you have selected destination folder or if the image format is not supported!"
STRING_8 = "You have not selected the conversion type!"

IMAGETYPES = [(STRING_5, "*.jpg"), (STRING_5, "*.png")]

def selectDirectory():
    global directory
    directory = filedialog.askdirectory()

def loadFiles():
    global filenames
    filenames = filedialog.askopenfilenames(filetypes=IMAGETYPES)
    
def startConversion():
    if dropdown_var.get() != STRING_3:
        try:
            for file in filenames:
                loc, ext = os.path.splitext(file)
                name = Path(loc).stem  
                Image.open(file).convert('RGB').save(directory + "/" + name + '.' + dropdown_var.get().lower())

        except:
            messagebox.showerror(STRING_6, STRING_7)
            
    else:
        messagebox.showerror(STRING_6, STRING_8)
        

class Frame(customtkinter.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root)

class Window(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self._set_appearance_mode("System")
        self.geometry("1280x720")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        self.main_frame = Frame(root=self)
        self.main_frame.grid(padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_propagate(False)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure((0, 1), weight=1)

        input_frame = Frame(root=self.main_frame)
        input_frame.grid(row=0, column=0, padx=10, pady=10, ipadx=256, ipady=256, sticky='w')
        input_frame.grid_propagate(False)
        input_frame.grid_rowconfigure(0, weight=8)
        input_frame.grid_rowconfigure(1, weight=1)
        input_frame.grid_columnconfigure((0, 1), weight=1)

        output_frame = Frame(root=self.main_frame)
        output_frame.grid(row=0, column=1, padx=10, pady=10, ipadx=256, ipady=256, sticky='e')
        output_frame.grid_propagate(False)
        output_frame.grid_rowconfigure(0, weight=1)
        output_frame.grid_rowconfigure(1, weight=8)
        output_frame.grid_columnconfigure(0, weight=1)
        output_frame.grid_columnconfigure(1, weight=1)

        # Input frame widgets
        button_selectf = customtkinter.CTkButton(master=input_frame, 
                                                 width=200, 
                                                 height=40, 
                                                 text=STRING_1,
                                                 command=loadFiles)
        button_selectf.grid(row=1, column=0, padx=50, pady=5, sticky='w')

        button_start = customtkinter.CTkButton(master=input_frame, 
                                               width=200, 
                                               height=40, 
                                               text=STRING_2,
                                               command=startConversion)
        button_start.grid(row=1, column=1, padx=50, pady=5, sticky='e')

        # Output frame widgets
        global dropdown_var
        dropdown_var = customtkinter.StringVar(value=STRING_1)
        dropdown = customtkinter.CTkOptionMenu(master=output_frame, 
                                               width=200,
                                               height=40,
                                               values=["PNG", "JPEG"], 
                                               variable=dropdown_var)
        dropdown.grid(row=0, column=0, padx=50, sticky='w')
        dropdown.set(STRING_3)

        button_dest = customtkinter.CTkButton(master=output_frame, 
                                               width=200, height=40, 
                                               text=STRING_4,
                                               command=selectDirectory)
        button_dest.grid(row=0, column=1, padx=50, sticky='e')

if __name__ == "__main__":
    app = Window()
    app.mainloop()
