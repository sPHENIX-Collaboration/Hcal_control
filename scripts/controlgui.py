# Script to run gui to control sPHENIX hadronic calorimeters
# Dan Richford (Baruch/CUNY, 2022-12-12-M)
# Python Version (queried on opc0.rhic.bnl.gov on 2022-12-12):
#   phnxrc@opc0:~/drichf1/scripts$ python -V
#   Python 2.7.16
#
from Tkinter import *
import os
import sys

# list of button names and their associated shell commands

hcalcommands = [
    ["GET TEMPS","python /home/phnxrc/drichf1/control/hcaltemp_all.py"]
    ] # close array of hcal commands

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        homedir = os.getenv('HOME','/')
        # logo_image = homedir + "/drichf1/sphenix-logo-white-bg.gif"
        # print logo_image

        try:
            f = open( logo_image )
            f.close()
            logo = PhotoImage(file=logo_image)
            self.lbl = Label( frame, image=logo, text="sPHENIX" )
            self.lbl.logo = logo
        except IOError:
            print 'error opening logo: ', logo_image, ' ... ignoring'
            self.lbl = Label( frame, text="sPHENIX" )

        self.lbl.configure(background='white')
        self.lbl.pack(side=TOP,fill=X)

        button_frame = Frame(frame)
        exit_frame = Frame(frame)

        button_frame.pack(side=TOP,fill=X)
        exit_frame.pack(side=TOP,fill=X)

        left_frame = Frame(button_frame)
        middle_frame = Frame(button_frame)
        right_frame = Frame(button_frame)

        left_frame.pack(side=LEFT,fill=BOTH)
        middle_frame.pack(side=LEFT,fill=BOTH)
        right_frame.pack(side=RIGHT,fill=BOTH)

        for c in hcalcommands:
            self.sh = Button( right_frame, text=c[0],
                              command=lambda arg1=c[1]: self.shell(arg1),
                              anchor=W )
            self.sh.pack(side=TOP,fill=X)

        self.quit = Button(exit_frame, text="Exit", command=frame.quit, anchor=CENTER)
        self.quit.pack(side=TOP,fill=X)

    #Execute shell command "x" and print result
    def shell(self,x):
        result=os.system( x )

# MAIN
root = Tk()
root.title("HCAL@1008")
app = App(root)

root.mainloop()

