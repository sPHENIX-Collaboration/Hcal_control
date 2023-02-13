#!/bin/python3

import sys
import telnetlib
import sqlite3
import datetime
import time

print("This script reads the 'everything' \nin the EMCal style\nof all sectors using the $Ec command!")
print("EXPERIMENTAL! THIS COMMAND MAY DISTURB THINGS YOU HAVE SET PREVIOUSLY OR WILL SET IN YOUR NEXT FEW COMMANDS!"
      
if len(sys.argv) == 2:
    print("Usage: test_pulse.py {outer|inner|both} {east|west|all}")
    sys.exit(0)

arg_detector = str(sys.argv[1]).lower()
arg_half = str(sys.argv[2]).lower()


host_prefix = "10.20.34."
port_number = "9760"
hosts_outer_east = ["80","81","82","83"]
hosts_outer_west = ["90","91","92","93"]
hosts_inner_east = ["84","85","86","87"]
hosts_inner_west = ["94","95","96","97"]

if(arg_detector=="both" and arg_half=="all"):
    hosts = hosts_outer_east + hosts_inner_east + hosts_outer_west + hosts_inner_west

elif(arg_detector=="outer" and arg_half=="west"):
    hosts = hosts_outer_west

elif(arg_detector=="inner" and arg_half=="west"):
    hosts = hosts_inner_west

elif(arg_detector=="outer" and arg_half=="east"):
    hosts = hosts_outer_east

elif(arg_detector=="inner" and arg_half=="east"):
    hosts = hosts_inner_east

elif(arg_detector=="both" and arg_half=="west"):
    hosts = hosts_outer_west + hosts_inner_west

elif(arg_detector=="both" and arg_half=="east"):
    hosts = hosts_outer_east + hosts_inner_east
    
elif(arg_detector=="outer" and arg_half=="all"):
    hosts = hosts_outer_east + hosts_inner_west

elif(arg_detector=="inner" and arg_half=="all"):
    hosts = hosts_inner_east + hosts_inner_west

else:
    print("please select ./gain.py [outer|inner|both] [east|west|all]")
    sys.exit(1)


# Detector settings
gain_command = "$E"

for h in hosts:
    try:
        tn = telnetlib.Telnet(host_prefix+h,port_number)
    except TelnetException as ex:
        print(ex)
        print("cannont connect to controller board @" + h + "...give up.")
        sys.exit()

    tn.write(b"\n\r")
    tn.write(b"\n\r")
    
    print("Everything for  "+host_prefix+h)
    for c in range(8):
        # Gain
        tn.write(bytes(gain_command+str(c),encoding="ascii"))
        g = tn.read_until(b">")
        print(g)
        tn.write(b"\n\r")
