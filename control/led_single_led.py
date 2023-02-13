#!/bin/python3

import sys
import telnetlib
import sqlite3
import datetime
import time

#from ledmask import ledmask
#from hcalgain import setgain

print("This script turns on/off the LED \nto all sectors using the $LMcbb command!")
print("Remember to set the gain on all channels to 'NORMAL' if using all LEDs! ('HIGH' if only one.)")

if len(sys.argv) == 3:
    print("Usage: test_pulse.py {outer|inner|both} {east|west|all} {on|0|1|2|3|4|off}")
    sys.exit(0)

arg_detector = str(sys.argv[1]).lower()
arg_half = str(sys.argv[2]).lower()
arg_status = str(sys.argv[3]).lower()

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
    print("please select ./led.y [outer|inner|both] [east|west|all] [on|0|1|2|3|4|off]")
    sys.exit(1)


# LED Settings
dac = 3200
#dac = 2900
dac_setting = str(dac)
dac_command = "$LS"
nleds = 5

mask_command = "$LM"
if(arg_status=="on"):
    print("echo")
    mask_setting = "001F"
elif(arg_status=="0"):
    mask_setting = "0001"
elif(arg_status=="1"):
    mask_setting = "0002"
elif(arg_status=="2"):
    mask_setting = "0004"
elif(arg_status=="3"):
    mask_setting = "0008"
elif(arg_status=="4"):
    mask_setting = "0010"
elif(arg_status=="off"):
    mask_setting = "0000"
else:
    print("LED mask error! Please use only 'on,' '0,' '1,' '2,' '3,' '4,' or 'off.'")
    sys.exit(2)

for h in hosts:
    try:
        tn = telnetlib.Telnet(host_prefix+h,port_number)
    except TelnetException as ex:
        print(ex)
        print("cannont connect to controller board @" + h + "...give up.")
        sys.exit()

    tn.write(b"\n\r")
    tn.write(b"\n\r")

    for c in range(8):        
        # LED Intensity
        for l in range(nleds):
            print("Sending: "+dac_command+str(c)+str(l)+dac_setting)
            tn.write(bytes(dac_command+str(c)+dac_setting,encoding="ascii"))
            #gg= tn.read_until(b">") # this command has no output, but requires a new line/carriage return
            #print(gg)
            tn.write(b"\n\r")
            tn.write(b"\n\r")

        # LED Mask
        print("Sending: "+mask_command+str(c)+mask_setting)
        tn.write(bytes(mask_command+str(c)+mask_setting,encoding="ascii"))
        ggg= tn.read_until(b">")
        print(ggg)
        tn.write(b"\n\r")

    print("Intensity "+dac_setting+" for "+host_prefix+h)
    print("Tiles "+mask_setting+" for "+host_prefix+h)
