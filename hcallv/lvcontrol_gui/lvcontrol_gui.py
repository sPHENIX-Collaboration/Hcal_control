from tkinter import Tk, Label, IntVar, StringVar, Checkbutton, Button, Frame, font

def binary_to_hex(binary_string):
    decimal = int(binary_string, 2)
    return "{:0>2X}".format(decimal)

def create_command_string(board_id, setting):
    return "$E"+"{:02d}".format(board_id+1)+binary_to_hex(setting[::-1])

def turn_on_board(board_id, setting):
    print("board id:", board_id, "settings:", setting, "command string:", create_command_string(board_id, setting))
    ## send command via telnet!

def read_voltages():
    return [[0 for _ in range(16)] for _ in range(16)]

class LowVoltagePowerSupplyGUI:
    def __init__(self, master):

        voltages = read_voltages()

        # Set font
        font.nametofont("TkDefaultFont").configure(family="Arial", size=12)

        # Measure width of voltage values to set cell width
        # create a font object
        #font_object = font.Font(family="Arial", size=12)
        cell_width = 5 #font_object.measure("+6.67")

        self.master = master
        master.title("Low Voltage Power Supply Control")

        # Create OHCal frame

        ohcal_frame = Frame(master)
        ohcal_frame.grid(row=0,column=0)

        # Create labels
        ohcal_label = Label(ohcal_frame, text="OHCal boards", font=("Arial",20))
        ohcal_label.grid(row=0, column=0+1, columnspan=24)

        # Create the checkboxes for each channel
        self.checkboxes = [[IntVar() for _ in range(16)] for _ in range(8)]
        self.markers = [[None for _ in range(32)] for _ in range(8)]
        self.markers_state = [[0 for _ in range(16)] for _ in range(8)]
        
        for col in range(8):
            Label(ohcal_frame,
            text="{}".format(col+1)).grid(row=1,column=3*col+2,columnspan=2)

        for row in range(8):
            Label(ohcal_frame, text="{}".format(row+1)).grid(row=row+2,column=0)

        for row in range(8):
            for col in range(8):

                pos_voltage = voltages[col][2*row]
                neg_voltage = voltages[col][2*row+1]

                pos_color, neg_color, checkbox_state = self.get_colors_and_state(pos_voltage,neg_voltage)
                self.checkboxes[row][col].set(checkbox_state)

                Checkbutton(ohcal_frame, variable=self.checkboxes[row][col]).grid(row=row+2,column=3*col+1)
                self.markers[row][2*col] = Label(ohcal_frame, height=1,
                bg=pos_color,text="{:.2f}".format(pos_voltage),width=cell_width)
                self.markers[row][2*col].grid(row=row+2,column=3*col+1+1,ipadx=2) 

                self.markers[row][2*col+1] = Label(ohcal_frame, height=1, bg=neg_color,
                text="{:.2f}".format(neg_voltage),width=cell_width)
                self.markers[row][2*col+1].grid(row=row+2,column=3*col+2+1,ipadx=2)
               
        # Create IHCal frame
        ihcal_frame = Frame(master)
        ihcal_frame.grid(row=1,column=0)

        # Create labels
        ihcal_label = Label(ihcal_frame, text="IHCal boards", font=("Arial",20))
        ihcal_label.grid(row=0, column=0+1, columnspan=24)

       
        for col in range(8,16):
            Label(ihcal_frame,
            text="{}".format(col+1)).grid(row=1,column=3*(col-8)+2,columnspan=2)

        for row in range(8):
            Label(ihcal_frame, text="{}".format(row+1)).grid(row=row+2,column=0)

        for row in range(8):
            for col in range(8,16):

                pos_voltage = voltages[col][2*row]
                neg_voltage = voltages[col][2*row+1]

                pos_color, neg_color, checkbox_state = self.get_colors_and_state(pos_voltage,neg_voltage)
                self.checkboxes[row][col].set(checkbox_state)

                Checkbutton(ihcal_frame,
                variable=self.checkboxes[row][col]).grid(row=row+2,column=3*(col-8)+1)
                self.markers[row][2*col] = Label(ihcal_frame, height=1,
                bg=pos_color,text="{:.2f}".format(pos_voltage),width=cell_width)
                self.markers[row][2*col].grid(row=row+2,column=3*(col-8)+1+1,ipadx=2) 

                self.markers[row][2*col+1] = Label(ihcal_frame, height=1, bg=neg_color,
                text="{:.2f}".format(neg_voltage),width=cell_width)
                self.markers[row][2*col+1].grid(row=row+2,column=3*(col-8)+2+1,ipadx=2)


        # Create a button to turn on the selected channels
        self.turn_on_button = Button(master, text="Turn On", command=self.turn_on_boards)
        self.turn_on_button.grid(row=8+1+1, column=0, columnspan=8)

    def turn_on_boards(self):
        for board_id in range(16):
            call_board = False
            for channel in range(8):
                settings = "".join("1" if self.checkboxes[channel][board_id].get() else "0" for channel in range(8))
                if self.checkboxes[channel][board_id].get():
                    self.markers[channel][board_id*2].config(bg="green")
                    self.markers[channel][board_id*2+1].config(bg="green")

                    if self.markers_state[channel][board_id] != int(self.checkboxes[channel][board_id].get()):
                        call_board = True
                        self.markers_state[channel][board_id] = 1
                else:
                    self.markers[channel][board_id*2].config(bg="white")
                    self.markers[channel][board_id*2+1].config(bg="white")
                    if self.markers_state[channel][board_id] != int(self.checkboxes[channel][board_id].get()):
                        call_board = True
                        self.markers_state[channel][board_id] = 0
            if call_board:
                turn_on_board(board_id, settings)


    def get_colors_and_state(self, pos_voltage, neg_voltage):
        pos_color = "white"
        neg_color = "white"
        checkbox_state = 0

        if pos_voltage > 0.1:
            checkbox_state = 1
            if pos_voltage > 6.0:
                pos_color = "green"
            else:
                pos_color = "yellow"

            if neg_voltage > -0.1:
                neg_color = "red"

        if neg_voltage < -0.1:
            checkbox_state = 1
            if neg_voltage < -6.0:
                neg_color = "green"
            else:
                neg_color = "yellow"

            if pos_voltage < 0.1:
                pos_color = "red"
            
        return (pos_color, neg_color, checkbox_state)

        



root = Tk()
gui = LowVoltagePowerSupplyGUI(root)
root.mainloop()
