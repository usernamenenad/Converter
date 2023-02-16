import tkinter
import customtkinter
import converter
import constants
import ctypes

class Frame(customtkinter.CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root)

class Window(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

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
        converter.show_images_frame = customtkinter.CTkScrollableFrame(master=input_frame)
        converter.show_images_frame.grid(row=0, columnspan=2, padx=(30, 30), pady=20, ipadx=200, ipady=100, sticky='n')

        button_selectf = customtkinter.CTkButton(master=input_frame, 
                                                 width=200, 
                                                 height=40, 
                                                 text=constants.STRING_LIST[0],
                                                 command=converter.loadFiles)
        button_selectf.grid(row=1, column=0, padx=50, pady=5, sticky='w')

        button_start = customtkinter.CTkButton(master=input_frame, 
                                               width=200, 
                                               height=40, 
                                               text=constants.STRING_LIST[1],
                                               command=converter.startConversion)
        button_start.grid(row=1, column=1, padx=50, pady=5, sticky='e')

        # Output frame widgets

        converter.dropdown_var = customtkinter.StringVar(value=constants.STRING_LIST[2])
        dropdown = customtkinter.CTkOptionMenu(master=output_frame, 
                                               width=200,
                                               height=40,
                                               values=["PNG", "JPEG"], 
                                               variable=converter.dropdown_var)
        dropdown.grid(row=0, column=0, padx=50, sticky='w')
        dropdown.set(constants.STRING_LIST[2])

        button_dest = customtkinter.CTkButton(master=output_frame, 
                                               width=200, height=40, 
                                               text=constants.STRING_LIST[3],
                                               command=converter.selectDirectory)
        button_dest.grid(row=0, column=1, padx=50, sticky='e')

if __name__ == "__main__":
    app = Window()
    app.mainloop()
