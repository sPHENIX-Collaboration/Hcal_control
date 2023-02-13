#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import time
import threading
import hvcontrol

def calculate_slot_channel(x,y):
    hcalid = -1

    # OHcal channels
    if y <= 3 and y+x*4 <= 31:
        hcalid = y+x*4
    # IHCal channels
    else:
        hcalid = 32+(y-4)+x*4

    slot = hcalid // 8
    channel = hcalid % 8

    return (slot, channel)

def set_voltage(x,y,voltage):
    slot, channel = calculate_slot_channel(x,y)
    hvcontrol.writechannel(what="outputVoltage",slot=slot,channel=channel,value=voltage)
       
def read_voltage(x,y):
    slot, channel = calculate_slot_channel(x,y)
    return hvcontrol.readchannel(what="outputVoltage",slot=slot,channel=channel)

def measure_voltage(x,y):
    slot, channel = calculate_slot_channel(x,y)
    return hvcontrol.readchannel(what="outputMeasurementSenseVoltage",slot=slot,channel=channel)

def set_state(x,y,state):
    slot, channel = calculate_slot_channel(x,y)
    hvcontrol.writechannel(what="outputSwitch",type='i',slot=slot,channel=channel,value=state)

def read_state(x,y):
    slot, channel = calculate_slot_channel(x,y)
    states = hvcontrol.channel_status(slot=slot,channel=channel)
    return states

def lock_all_widgets():
    for lb in lock_buttons:
        lb.config(state="disabled")
    for tf_row in calo_text_fields:
        for tf in tf_row:
            tf.config(state="disabled")
    for chb_row in checkboxes:
        for chb in chb_row:
            chb.config(state="disabled")

def unlock_all_widgets():
    for lb in lock_buttons:
        lb.config(state="normal")
    for tf_row in calo_text_fields:
        for tf in tf_row:
            tf.config(state="normal")
    for chb_row in checkboxes:
        for chb in chb_row:
            chb.config(state="normal")

def is_mainframe_on():
    return hvcontrol.mainframe_status()

def turn_mainframe_on():
    hvcontrol.mainframe_on_off("on")
    unlock_all_widgets()

def turn_mainframe_off():
    hvcontrol.mainframe_on_off("off")
    lock_all_widgets()


def init_text_fields(text_fields):
    for y in range(len(text_fields)):
        for x in range(len(text_fields[0])):
            #stored_voltage[y][x] = read_voltage(x,y)

            text_fields[y][x].delete(0, tk.END)
            text_fields[y][x].insert(0, "{:.2f}".format(read_voltage(x,y))
            text_fields[y][x].config(state='disabled')

def init_checkboxes(checkboxes):
    for y in range(len(checkboxes)):
        for x in range(len(checkboxes[0])): 
            if read_state(x,y):
                checkboxes[y][x].select()
            else:
                checkboxes[y][x].deselect()
            checkboxes[y][x].config(state='disabled')

def submit_commands(text_fields):
    for y in range(len(text_fields)):
        for x in range(len(text_fields[0])):
            text = text_fields[y][x].get()
            try:
                if text == "":
                    voltage = 0
                else:
                    voltage = float(text)
                
                if abs(voltage - read_voltage(x,y)) > 0.1:
                    #print("Voltage for channel ",x,y," set to ",voltage)                     
                    set_voltage(x,y,voltage)

                state = checkbox_state[y][x].get()
                if state != read_state(x,y):
                    set_state(x,y,state)


            except ValueError:
                print("Invalid value for channel ", x, y)
                text_fields[y][x].config(bg='red')
            
            #color = text_fields[y][x].cget("bg")
            #if color != 'white' and color != '#ffffff':
            #    text_fields[y][x].config(state='disable',disabledbackground=color)
            #else:
            
            text_fields[y][x].config(state='disable',disabledbackground='#d9d9d9')
            checkboxes[y][x].config(state='disable')

def unlock_all(text_fields):
    for y in range(len(text_fields)):
        for x in range(len(text_fields[0])):
            text_fields[y][x].config(state='normal')
            checkboxes[y][x].config(state='normal')


def fill_all(text_fields):
    voltage = float(fill_all_text_field.get())
    for y in range(len(text_fields)):
        for x in range(len(text_fields[0])):
            text_fields[y][x].delete(0, tk.END)
            text_fields[y][x].insert(0, voltage)

def turn_all_checkboxes(checkb, on_off):
    if on_off == "on":
        for chb_row in checkb:
            for chb in chb_row:
                chb.select()
    elif on_off == "off":
        for chb_row in checkb:
            for chb in chb_row:
                chb.deselect()


def open_file():
    file_path = filedialog.askopenfilename(initialdir="/home/phnxrc/drichf1/mpod/voltage_text_files",filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        with open(file_path, 'r') as file:
            contents = file.readlines()
            # Read line-by-line
            for i,line in enumerate(contents):
                y = None
                x = None
                if i < 32:
                    x = i // 4
                    y = i % 4
                else:
                    x = (i-32) // 4
                    y = i % 4 + 4

                calo_text_fields[y][x].delete(0, tk.END)
                calo_text_fields[y][x].insert(0, line.split(" ")[1])


###############################################################
# Threading to update status GUI every 10 (?) seconds

def update_status_table():
    global status_labels
    while True:
        if not is_mainframe_on():
            continue

        for y in range(8):
            for x in range(8):
                voltage = measure_voltage(x,y)
                read_voltage = read_voltage(x,y)
                status  = read_state(x,y)

                status_labels[y][x].config(text="{:.2f}".format(voltage))

                if status == 0:
                    status_labels[y][x].config(bg="white")
                elif read_voltage > 0.1:
                    if abs(read_voltage - voltage) < 0.1:
                        status_labels[y][x].config(bg="green")
                    elif voltage > 0.1:
                        status_labels[y][x].config(bg="yellow")
                    else:
                        status_labels[y][x].config(bg="red")
                else:
                    if voltage > 0.1:
                        status_labels[y][x].config(bg="orange")
                    else:
                        status_labels[y][x].config(bg="white")

        threading.Event().wait(10) 


###############################################################

#stored_voltage = [[0 for i in range(8)] for j in range(8)]

###############################################################
# Tkinter script for GUI starts here
#
# Object-map:
# ->root:
#   ->status_gui_frame
#     * ohcal_status_title
#     ->ohcal_status_frame
#       * ohcal_status[][]
#     * ihcal_status_title
#     ->ihcal_status_frame
#       * ihcal_status[][]
#   ->controller_gui_frame
#     * ohcal_title
#     ->ohcal_voltages_frame
#       * ohcal_text_field[][] 
#       * ohcal_checkbox[][]
#     * ihcal_title
#     ->ihcal_voltages_frame
#       * ihcal_text_field[][]
#       * ihcal_checkbox[][]
#   ->button_gui_frame
#     * bunch of buttons here...
#
###############################################################

root = tk.Tk()
root.title("sPHENIX HCal HV control")
#root.geometry("690x380")

# Create ohcal column headers
headers = ["0-3","4-7","8-11","12-15","16-19","20-23","24-27","28-31"]

## Status GUI frame

status_gui_frame = tk.Frame(root)
status_gui_frame.grid(row=0, column=0)

status_labels = []

# OHCal status title
ohcal_status_title = tk.Label(status_gui_frame, text="Measured voltages in OHCal sectors",
font=("Arial",20))
ohcal_status_title.grid(row=0,column=0)

# OHCal status frame
ohcal_status_frame = tk.Frame(status_gui_frame)
ohcal_status_frame.grid(row=1,column=0)

# OHCal status headers
for x in range(8):
    ohcal_status_header = tk.Label(ohcal_status_frame, text=headers[x])
    ohcal_status_header.grid(row=0, column=x)

for y in range(4):
    row = []
    for x in range(8):
        ohcal_status = tk.Label(ohcal_status_frame, width=10)
        ohcal_status.grid(row=y+1, column=x)
        row.append(ohcal_status)
    status_labels.append(row)

# IHCal status title
ihcal_status_title = tk.Label(status_gui_frame, text="Measured voltages in IHCal sectors",
font=("Arial",20))
ihcal_status_title.grid(row=2,column=0)

# IHCal status frame
ihcal_status_frame = tk.Frame(status_gui_frame)
ihcal_status_frame.grid(row=3,column=0)

# IHCal status headers
for x in range(8):
    ihcal_status_header = tk.Label(ihcal_status_frame, text=headers[x])
    ihcal_status_header.grid(row=0, column=x)


for y in range(4):
    row = []
    for x in range(8):
        ihcal_status = tk.Label(ihcal_status_frame, width=10)
        ihcal_status.grid(row=y+1, column=x)
        row.append(ihcal_status)
    status_labels.append(row)

## Controller GUI

controller_gui_frame = tk.Frame(root)
controller_gui_frame.grid(row=1, column=0)

# OHCal controller title

ohcal_title = tk.Label(controller_gui_frame, text="OHCal sectors", font=("Arial",20))
ohcal_title.grid(row=0, column=0)

# OHCal controller frame

ohcal_voltages_frame = tk.Frame(controller_gui_frame)
ohcal_voltages_frame.grid(row=1, column=0)

calo_text_fields = []
checkboxes = []

checkbox_state = [[0 for i in range(8)] for j in range(8)]

for y in range(8):
    for x in range(8):
        checkbox_state[y][x] = tk.IntVar(controller_gui_frame) 



for x in range(8):
    ohcal_header = tk.Label(ohcal_voltages_frame, text=headers[x])
    ohcal_header.grid(row=0, column=2*x+1)

# Create an 8x8 grid of text fields and checkboxes for OHcal
for y in range(4):
    chb_row = []
    row = []
    for x in range(8):

        ohcal_checkbox = tk.Checkbutton(ohcal_voltages_frame, variable=checkbox_state[y][x])
        ohcal_checkbox.grid(row=y+1, column=2*x)

        ohcal_text_field = tk.Entry(ohcal_voltages_frame,width=10)
        ohcal_text_field.grid(row=y+1, column=2*x+1)
        
        chb_row.append(ohcal_checkbox)
        row.append(ohcal_text_field)

    checkboxes.append(chb_row)
    calo_text_fields.append(row)

# IHCal title
ihcal_label = tk.Label(controller_gui_frame, text="IHCal sectors", font=("Arial",20))
ihcal_label.grid(row=2, column=0)

# IHCal controller frame
ihcal_voltages_frame = tk.Frame(controller_gui_frame)
ihcal_voltages_frame.grid(row=3, column=0)

for x in range(8):
    ihcal_header = tk.Label(ihcal_voltages_frame, text=headers[x])
    ihcal_header.grid(row=0, column=2*x+1)

# Create an 8x8 grid of text fields for IHCAL
for y in range(4):
    chb_row = []
    row = []
    for x in range(8):
        
        ihcal_checkbox = tk.Checkbutton(ihcal_voltages_frame, variable=checkbox_state[y+4][x])
        ihcal_checkbox.grid(row=y+1, column=2*x)

        ihcal_text_field = tk.Entry(ihcal_voltages_frame,width=10)
        ihcal_text_field.grid(row=y+1, column=2*x+1)

        chb_row.append(ihcal_checkbox)
        row.append(ihcal_text_field)

    checkboxes.append(chb_row)
    calo_text_fields.append(row)


check_vars = [tk.BooleanVar() for i in range(9)]
#ihcal_checkbox_columns = list(zip(*(checkboxes[4:])))

#print(ihcal_checkbox_columns)

#checkbox_columns = []

#checkbox_column_state = [tk.BooleanVar() for i in range(8)]

# Adding checkboxes to check a whole column at once
#for x in range(8):
#    ihcal_column_checkbox = tk.Checkbutton(ihcal_voltages_frame, variable=checkbox_column_state[x], command=lambda:
#    turn_all_checkboxes([ihcal_checkbox_columns[x]],"on"))
#    ihcal_column_checkbox.grid(row=5,column=2*x)
#    checkbox_columns.append(ihcal_column_checkbox)



## Button GUI frame

button_gui_frame = tk.Frame(root)
button_gui_frame.grid(row=3, column=0)

# A list of locakble buttons
lock_buttons = []

# Create fill all button
fill_all_button = tk.Button(button_gui_frame, text="Fill All", width=15, command=lambda:
fill_all(calo_text_fields))
fill_all_button.grid(row=0, column=2)
lock_buttons.append(fill_all_button)

# Create fill OHCal button
fill_ohcal_button = tk.Button(button_gui_frame, text="Fill OHCal", width=15, command=lambda:
fill_all(calo_text_fields[:4]))
fill_ohcal_button.grid(row=0, column=3)
lock_buttons.append(fill_ohcal_button)

# Create fill IHCal button
fill_ihcal_button = tk.Button(button_gui_frame, text="Fill IHCal", width=15, command=lambda:
fill_all(calo_text_fields[4:]))
fill_ihcal_button.grid(row=0, column=4)
lock_buttons.append(fill_ihcal_button)

# Create fill all, text field 
fill_all_text_field = tk.Entry(button_gui_frame,width=10)
fill_all_text_field.grid(row=0, column=5)
lock_buttons.append(fill_all_text_field)

# Turn on all checkboxes button
turn_on_checkboxes = tk.Button(button_gui_frame, text="Turn On All", width=15, command=lambda:
turn_all_checkboxes(checkboxes,"on"))
turn_on_checkboxes.grid(row=1, column=2)
lock_buttons.append(turn_on_checkboxes)

# Turn on all OHCal checkboxes button
turn_on_ohcal_checkboxes = tk.Button(button_gui_frame, text="Turn On OHCal", width=15, command=lambda:
turn_all_checkboxes(checkboxes[:4],"on"))
turn_on_ohcal_checkboxes.grid(row=1, column=3)
lock_buttons.append(turn_on_ohcal_checkboxes)

# Turn on all IHCal checkboxes button
turn_on_ihcal_checkboxes = tk.Button(button_gui_frame, text="Turn On IHCal", width=15, command=lambda:
turn_all_checkboxes(checkboxes[4:],"on"))
turn_on_ihcal_checkboxes.grid(row=1, column=4)
lock_buttons.append(turn_on_ihcal_checkboxes)

# Turn off all checkboxes button
turn_off_checkboxes = tk.Button(button_gui_frame, text="Turn Off All", width=15, command=lambda:
turn_all_checkboxes(checkboxes,"off"))
turn_off_checkboxes.grid(row=2, column=2)
lock_buttons.append(turn_off_checkboxes)

# Turn off all OHCal checkboxes button
turn_off_ohcal_checkboxes = tk.Button(button_gui_frame, text="Turn Off OHCal", width=15, command=lambda:
turn_all_checkboxes(checkboxes[:4],"off"))
turn_off_ohcal_checkboxes.grid(row=2, column=3)
lock_buttons.append(turn_off_ohcal_checkboxes)

# Turn off all IHCal checkboxes button
turn_off_ihcal_checkboxes = tk.Button(button_gui_frame, text="Turn Off IHCal", width=15, command=lambda:
turn_all_checkboxes(checkboxes[4:],"off"))
turn_off_ihcal_checkboxes.grid(row=2, column=4)
lock_buttons.append(turn_off_ihcal_checkboxes)




# Create unlock all button 
unlock_all_button = tk.Button(button_gui_frame, text="Unlock All", width=15, command=lambda: unlock_all(calo_text_fields))
unlock_all_button.grid(row=3, column=2)
lock_buttons.append(unlock_all_button)

# Load from file button
load_button = tk.Button(button_gui_frame, text="Load file", command=open_file, width=15)
load_button.grid(row=3, column=3)

# Refresh button 
refresh_button = tk.Button(button_gui_frame, text="Refresh", width=15, command=lambda:
(init_text_fields(calo_text_fields),init_checkboxes(checkboxes)))
refresh_button.grid(row=3, column=4)
lock_buttons.append(refresh_button)

# Create set voltage button
set_voltage_button = tk.Button(button_gui_frame, text="Set", width=15, command=lambda:
submit_commands(calo_text_fields))
set_voltage_button.grid(row=3, column=5)
lock_buttons.append(set_voltage_button)



# Create a turn mainframe on button

# Check if mainframe is on

mainframe_button = tk.Button(button_gui_frame, width=15)

if is_mainframe_on():
    mainframe_button.config(text="Turn off mainframe")
    init_text_fields(calo_text_fields)
    init_checkboxes(checkboxes)
else:
    mainframe_button.config(text="Turn on mainframe")
    lock_all_widgets()

mainframe_button.grid(row=0,column=1)

# Change the state of the mainframe button
def change_state():
    if mainframe_button['text'] == "Turn on mainframe":
        turn_mainframe_on()
        time.sleep(3)
        mainframe_button.config(text="Turn off mainframe")
        init_text_fields(calo_text_fields)
        init_checkboxes(checkboxes)
    else:
        turn_mainframe_off()
        mainframe_button.config(text="Turn on mainframe")

mainframe_button.config(command=change_state)

thread = threading.Thread(target=update_status_table)
thread.start()

root.mainloop()
