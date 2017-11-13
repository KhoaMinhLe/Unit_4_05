# Created by: Khoa Le
# Created on November 7 2017
# Created for ICS3U
# This program calculates the volume of a cylinder.

import ui

PI = 3.14

def calculate_button(sender):
    user_input_height = int(view['user_height_textfield'].text)
    user_input_radius = int(view['user_radius_textfield'].text)
    
    answer_output = 2.00*PI*user_input_radius**2.00*user_input_height
    
    view['answer_label'].text = str(answer_output)

view = ui.load_view()
view.present('sheet')
