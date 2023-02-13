#!/bin/python3

import sys
import telnetlib
import sqlite3
import datetime
import time

print("This script reads the test pulse \nto all sectors using the $Pcbb command!")
print("EXPERIMENTAL: THIS SCRIPT MAY UN-SET THE\nTEST-PULSE MASK TO CHANNEL 7!")
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

elif(arg_detector=="both" and arg_half=="west"):
    hosts = hosts_outer_west + hosts_inner_west

elif(arg_detector=="outer" and arg_half=="east"):
    hosts = hosts_outer_east

elif(arg_detector=="inner" and arg_half=="east"):
    hosts = hosts_inner_east

elif(arg_detector=="both" and arg_half=="east"):
    hosts = hosts_outer_east + hosts_inner_east

else:
    print("please select ./test_pulse.py [outer|inner|both] [east|west|all] [on|off]")
    sys.exit(1)


# Pulse Settings    
command_string = "$P"
for h in hosts:
    print("TP for "+host_prefix+h)
    try:
        tn = telnetlib.Telnet(host_prefix+h,port_number)
    except TelnetException as ex:
        print(ex)
        print("cannont connect to controller board @" + h + "...give up.")
        sys.exit()

    tn.write(b"\n\r")
    tn.write(b"\n\r")


    # Pulse Mask
    tn.write(bytes(command_string,encoding="ascii"))
    tn.write(b"\n\r")
    g = tn.read_until(b">") # do not comment out: otherwise, prior commands overwritten
    print(g)
    tn.write(b"\n\r")

