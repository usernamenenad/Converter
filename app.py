import window
import converter
import constants

if __name__ == '__main__':
    app = window.Window('System', '1280x720', [False, False], 'Converter 1.0')

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    cfb = app.add_button(app.input_frame, name='Choose files button',
                         wh=constants.DEFAULT_BUTTON_WH, 
                         text=constants.STRING_LIST[0],
                         command=converter.loadFiles,
                         rc = [1, 0],
                         padxy=constants.DEFAULT_BUTTON_PADXY,
                         sticky='w')
    
    scb = app.add_button(app.input_frame, name="Start conversion button",
                         wh=constants.DEFAULT_BUTTON_WH,
                         text=constants.STRING_LIST[1],
                         command=converter.startConversion,
                         rc=[1, 1],
                         padxy=constants.DEFAULT_BUTTON_PADXY,
                         sticky='e')
    
    converter.show_images_frame = app.add_scrollable_frame(app.input_frame, name="Scrollable frame showing files",
                                                           rc=[0, 0], padxy=[(30, 30), 35],
                                                           ipadxy=[200, 100],
                                                           sticky='n')
    converter.show_images_frame.grid(columnspan=2)
    
    #Output frame widgets
    scd, converter.dropdown_var = app.add_dropdown(app.output_frame, name='Select conversion type dropdown',
                                                   valuevar=constants.STRING_LIST[2],
                                                   wh=constants.DEFAULT_BUTTON_WH,
                                                   values=constants.SUPPORTED_TYPES,
                                                   rc=[0, 0],
                                                   padxy=[50, 0],
                                                   sticky='e')
    
    sdb = app.add_button(app.output_frame, name='Select destination folder button',
                         wh=constants.DEFAULT_BUTTON_WH,
                         text=constants.STRING_LIST[3],
                         command=converter.selectDirectory,
                         rc=[0, 1],
                         padxy=[50, 0],
                         sticky='e')
    
    app.mainloop()
