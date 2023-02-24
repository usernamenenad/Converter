import tkinter
import customtkinter
import constants
import ctypes

class Frame(customtkinter.CTkFrame):
    def __init__(self, root):
        
        super().__init__(master=root)
        
        super().grid_propagate(False)

    def frame_settings(self, **kwargs):
        
        if kwargs.get('rc') != None:
            self.grid(row=kwargs['rc'][0], column=kwargs['rc'][1])

        if kwargs.get('wh') != None:
            self.configure(width=kwargs['wh'][0], height=kwargs['wh'][1])

        if kwargs.get('padxy') != None:
            self.grid(padx=kwargs['padxy'][0], pady=kwargs['padxy'][1])

        if kwargs.get('ipadxy') != None:
            self.grid(ipadx=kwargs['ipadxy'][0], ipady=kwargs['ipadxy'][1])

        if kwargs.get('sticky') != None:
            self.grid(sticky=kwargs['sticky'])

        if kwargs.get('fg_color') != None:
            self.configure(fg_color=kwargs['fg_color'])
        
        if kwargs.get('rowcon') != None:
            i = 0
            for row in kwargs['rowcon']:
                self.grid_rowconfigure(row, weight=kwargs['rweight'][i])
                i+=1

        if kwargs.get('colcon') != None:
            i = 0
            for column in kwargs['colcon']:
                self.grid_columnconfigure(column, weight=kwargs['cweight'][i])
                i+=1

class Window(customtkinter.CTk):

    def __init__(self, app_mode, res, resizable, title):
        super().__init__()
        
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        self.title(title)
        self._set_appearance_mode(app_mode)
        self.geometry(res)
        self.resizable(resizable[0], resizable[1])
        self.font = customtkinter.CTkFont(family='Uni Sans')
        
        # App's main frame
        self.main_frame = Frame(self)
        self.main_frame.frame_settings(rowcon=[0], rweight=[1], 
                                       colcon=[0, 1], cweight=[1, 1],
                                       padxy=[20, 20],
                                       sticky='nsew')
        
        # App's input frame, fixed on main frame
        self.input_frame = Frame(self.main_frame)
        self.input_frame.frame_settings(rc=[0, 0], 
                                        rowcon=[0, 1], rweight=[8, 1], 
                                        colcon=[0, 1], cweight=[1, 1],
                                        padxy=[10, 10], ipadxy=[256, 256],
                                        sticky='w') 
        
        # App's output frame, fixed on main frame
        self.output_frame = Frame(self.main_frame)
        self.output_frame.frame_settings(rc=[0, 1],
                                         rowcon=[0, 1], rweight=[1, 8],
                                         colcon=[0, 1], cweight=[1, 1],
                                         padxy=[10, 10], ipadxy=[256, 256], 
                                         sticky='e')

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
                                         font = self.font,
                                         command=kwargs['command'])
        button.grid(row=kwargs['rc'][0], column=kwargs['rc'][1], 
                            padx=kwargs['padxy'][0], pady=kwargs['padxy'][1], 
                            sticky=kwargs['sticky'])
        
        self.update_wgt_list(frame, name, button)

        return button

    def add_dropdown(self, frame, name, **kwargs):
        var = customtkinter.StringVar(value=kwargs['valuevar'])
        dropdown = customtkinter.CTkOptionMenu(master=frame, 
                                               width=kwargs['wh'][0],
                                               height=kwargs['wh'][1],
                                               font = self.font,
                                               values=kwargs['values'], 
                                               variable=var)
        dropdown.grid(row=kwargs['rc'][0], column=kwargs['rc'][1], 
                      padx=kwargs['padxy'][0], pady=kwargs['padxy'][1], 
                      sticky=kwargs['sticky'])
        dropdown.set(constants.STRING_LIST[2])

        self.update_wgt_list(frame, name, dropdown)

        return dropdown, var

    def add_scrollable_frame(self, frame, name, **kwargs):
        scrollable = customtkinter.CTkScrollableFrame(master=frame)
        scrollable.grid(row=kwargs['rc'][0], column=kwargs['rc'][1],
                        padx=kwargs['padxy'][0], pady=kwargs['padxy'][1],
                        ipadx=kwargs['ipadxy'][0], ipady=kwargs['ipadxy'][1],
                        sticky=kwargs['sticky'])

        self.update_wgt_list(frame, name, scrollable)

        return scrollable
        
    def add_progress_bar(self, frame, name, **kwargs):
        progress_bar = customtkinter.CTkProgressBar(master=frame)
