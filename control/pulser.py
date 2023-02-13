#!/bin/python3

import sys
import telnetlib
import sqlite3
import datetime
import time

print("This script sets the pulse width to 100ns $Ptt command!")

if len(sys.argv) == 1:
    print("Usage: pulser.py [east|west|all]")
    sys.exit(0)

arg_half = str(sys.argv[1]).lower()

host_prefix = "10.20.34."
port_number = "9760"
hosts_west = ["113","112"]
hosts_east = ["111","110"]

if(arg_half=="all"):
    hosts = hosts_east + hosts_west
elif(arg_half=="west"):
    hosts = hosts_west
elif(arg_half=="east"):
    hosts = hosts_east + hosts_west
else:
    print("please use ./pulser [east|west|all].")
    sys.exit(1)

command_string = "$P"
setting_string = "100" # ns

for h in hosts:
    try:
        tn = telnetlib.Telnet(host_prefix+h,port_number)
    except TelnetException as ex:
        print(ex)
        print("cannont connect to pulser-fan-out board @" + h + "...give up.")
        sys.exit()

    tn.write(b"\n\r")
    tn.write(b"\n\r")
    
    print("Sending: "+command_string+setting_string)
    tn.write(bytes(command_string+setting_string,encoding="ascii"))
    #g = tn.read_until(b">") # command has no output
    # print(g)
    tn.write(b"\n\r")
    tn.write(b"\n\r")
    print("Pulse width for "+host_prefix+h+" set to "+setting_string+" ns!")
print("... If you want to change the frequency, change the modebits!")
