import tkinter
import customtkinter
import constants
import ctypes

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master,fg_color=kwargs['fg_color'], 
                         width=kwargs['wh'][0], height=kwargs['wh'][1])
        
        super().grid(row=kwargs['rc'][0], column=kwargs['rc'][1],
                     padx=kwargs['padxy'][0], pady=kwargs['padxy'][1],
                     sticky=kwargs['sticky'])
        
        super().grid_propagate(False)

class Window(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        self._set_appearance_mode("System")
        self.geometry("1280x720")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        self.main_frame = customtkinter.CTkFrame(master=self)
        self.main_frame.grid(padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_propagate(False)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure((0, 1), weight=1)

        self.input_frame = customtkinter.CTkFrame(master=self.main_frame)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, ipadx=256, ipady=256, sticky='w')
        self.input_frame.grid_propagate(False)
        self.input_frame.grid_rowconfigure(0, weight=8)
        self.input_frame.grid_rowconfigure(1, weight=1)
        self.input_frame.grid_columnconfigure((0, 1), weight=1)

        self.output_frame = customtkinter.CTkFrame(master=self.main_frame)
        self.output_frame.grid(row=0, column=1, padx=10, pady=10, ipadx=256, ipady=256, sticky='e')
        self.output_frame.grid_propagate(False)
        self.output_frame.grid_rowconfigure(0, weight=1)
        self.output_frame.grid_rowconfigure(1, weight=8)
        self.output_frame.grid_columnconfigure((0, 1), weight=1)

        # Input frame widgets
        #converter.show_images_frame = customtkinter.CTkScrollableFrame(master=self.input_frame)
        #converter.show_images_frame.grid(row=0, columnspan=2, padx=(30, 30), pady=20, ipadx=200, ipady=100, sticky='n')
        
        self.input_frame_widgets = {}
        self.output_frame_widgets = {}

    def update_wgt_list(self, frame, name, wgt):
        if(frame == self.input_frame):
            self.input_frame_widgets.update({name : wgt})
        if(frame == self.output_frame):
            self.output_frame_widgets.update({name : wgt})
    
    def add_button(self, frame, name, **kwargs):
        button = customtkinter.CTkButton(master=frame, 
                                                 width=kwargs['wh'][0], 
                                                 height=kwargs['wh'][1], 
                                                 text=kwargs['text'],
                                                 command=kwargs['command'])
        button.grid(row=kwargs['rc'][0], column=kwargs['rc'][1], 
                            padx=kwargs['padxy'][0], pady=kwargs['padxy'][1], 
                            sticky=kwargs['sticky'])
        
        self.update_wgt_list(frame, name, button)

        return button

    def add_dropdown(self, frame, name, **kwargs):
        kwargs['var'] = customtkinter.StringVar(value=kwargs['valuevar'])
        dropdown = customtkinter.CTkOptionMenu(master=frame, 
                                               width=kwargs['wh'][0],
                                               height=kwargs['wh'][1],
                                               values=kwargs['values'], 
                                               variable=kwargs['var'])
        dropdown.grid(row=kwargs['rc'][0], column=kwargs['rc'][1], 
                      padx=kwargs['padxy'][0], pady=kwargs['padxy'][1], 
                      sticky=kwargs['sticky'])
        dropdown.set(constants.STRING_LIST[2])

        self.update_wgt_list(frame, name, dropdown)

        return dropdown

    def add_scrollable_frame(self, frame, name, **kwargs):
        scrollable = customtkinter.CTkScrollableFrame(master=frame)
        scrollable.grid(row=kwargs['rc'][0], column=kwargs['rc'][1],
                        padx=kwargs['padxy'][0], pady=kwargs['padxy'][1],
                        ipadx=kwargs['ipadxy'][0], ipady=kwargs['ipadxy'][1],
                        sticky=kwargs['sticky'])

        self.update_wgt_list(frame, name, scrollable)

        return scrollable