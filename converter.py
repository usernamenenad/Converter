import customtkinter

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
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure((0, 1), weight=1)

        input_frame = Frame(root=self.main_frame)
        input_frame.grid(row=0, column=0, padx=10, pady=10, ipadx=256, ipady=256, sticky='w')
        input_frame.grid_propagate(False)

        input_frame.grid_rowconfigure(0, weight=8)
        input_frame.grid_rowconfigure(1, weight=1)
        input_frame.grid_columnconfigure((0, 1), weight=1)

        
        button_selectf = customtkinter.CTkButton(master=input_frame, width=200, height=50, text="Choose files")
        button_selectf.grid(row=1, column=0, padx=50, pady=5, sticky='w')

        button_start = customtkinter.CTkButton(master=input_frame, width=200, height=50, text="Start conversion")
        button_start.grid(row=1, column=1, padx=50, pady=5, sticky='e')

        out = Frame(root=self.main_frame)
        out.grid(row=0, column=1, padx=10, pady=10, ipadx=256, ipady=256, sticky='e')



    
if __name__ == "__main__":
    root = Window()
    root.mainloop()
