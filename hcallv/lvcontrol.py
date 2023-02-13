#!/bin/env python3

import sys
import telnetlib
import sqlite3
import time
import os.path
import time
import re
from datetime import datetime
from array import array

# John Haggerty, BNL, 2020.09.16

PORT = 9760

def lv_connect(HOST):
    try:
        tn = telnetlib.Telnet(HOST,PORT)
    except Exception as ex:
        print(ex)
        print("cannot connect to controller... give up")
        sys.exit()

    return tn

def lv_disconnect(tn):
    tn.close()

###########################################################
# Oliver's code to read voltages for quick status
def lv_readv_oliver(tn,slot):

    command = '$V'+f"{slot:02d}"
    tn.write(command.encode('ascii')+b"\n\r")
    x = tn.read_until(b'>')
#    print(x)
    
# the returned data look like this:
#    b'V01\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r'    
    line = x.decode('ascii')
# delete up to the V01 in above example
# re.DOTALL lets the match traverse \n and \r
#    line = re.sub('^.*?'+command[1:]+'\n\r', '', line, flags=re.DOTALL)
# remove some characters from the string that we don't need    
    line = line.replace('\n\r>', '')
    line = line.replace('\r', '')
    line = line.replace('V', '')
# split the string into strings of voltages    
    vstring = line.split('\n')
# get rid of blanks if they're there
    try:
        vstring.remove('')
        vstring.remove(' ')
    except ValueError:
        pass
#    print(vstring)
# convert the voltages as strings to floats     
#    print('voltages: ',voltages)
    if len(vstring) == 17:
        return vstring[1:]
    else:
        return vstring

############################################################
# Oliver's code for printing out status for channels
def status_report(tn):
    status = [ [0]*16 for i in range(8)]
    for s in range(16):
        voltage = lv_readv_oliver(tn,s+1)
        for i,v in enumerate(voltage):
            #v = str(v)
            if i >= 8:
                break
            elif float(v) > 1.0:
                status[i][s] = 1
    for s in status:
        print(s)

############################################################

def lv_readv(tn,slot):

    command = '$V'+f"{slot:02d}"
    tn.write(command.encode('ascii')+b"\n\r")
    x = tn.read_until(b'>')
#    print(x)
    
# the returned data look like this:
#    b'V01\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r0.000V\n\r'    
    line = x.decode('ascii')
# delete up to the V01 in above example
# re.DOTALL lets the match traverse \n and \r
#    line = re.sub('^.*?'+command[1:]+'\n\r', '', line, flags=re.DOTALL)
# remove some characters from the string that we don't need    
    line = line.replace('\n\r>', '')
    line = line.replace('\r', '')
    line = line.replace('V', '')
# split the string into strings of voltages    
    vstring = line.split('\n')
# get rid of blanks if they're there
    try:
        vstring.remove('')
        vstring.remove(' ')
    except ValueError:
        pass
#    print(vstring)
# convert the voltages as strings to floats     
    voltages = [float(v) for v in vstring]
#    print('voltages: ',voltages)
    return voltages

def lv_readi(tn,slot):

    command = '$I'+f"{slot:02d}"
    tn.write(command.encode('ascii')+b"\n\r")
    x = tn.read_until(b">")
    line = x.decode('ascii')
# delete up to the V01 in above example
# re.DOTALL lets the match traverse \n and \r
#    line = re.sub('^.*?'+command[1:]+'\n\r', '', line, flags=re.DOTALL)
# remove some characters from the string that we don't need    
    line = line.replace('\n\r>', '')
    line = line.replace('\r', '')
    line = line.replace('A', '')
# split the string into strings of voltages    
    istring = line.split('\n')
# get rid of blanks if they're there
    try:
        istring.remove('')
        istring.remove(' ')
    except ValueError:
        pass
# convert the voltages as strings to floats    
    currents = [float(i) for i in istring]
#    print('currents: ',currents)
    return currents

def lv_enable(tn,slot,onoroff):

    if onoroff == 0:
        command = '$E'+f"{slot:02d}"+str('00')
    else:
        command = '$E'+f"{slot:02d}"+str('FF')
         
    print(command)
    tn.write(command.encode('ascii')+b"\n\r")
    tn.read_until(b'>')

def lv_enable_single_channel(tn,slot,channel):
    command = '$E'+f"{slot:02d}"+channel #f"{channel:02d}"
    print(command)
    tn.write(command.encode('ascii')+b"\n\r")
    tn.read_until(b'>')

def lv_enable_combined_channels(tn,slot,combination_hexcode):
    command = '$E'+f"{slot:02d}"+combination_hexcode
    print(command)
    tn.write(command.encode('ascii')+b"\n\r")
    tn.read_until(b'>')

def lv_reset(tn):

    command = '$R'     
    print(command)
    tn.write(command.encode('ascii')+b"\n\r")

# main

def main():
    
    if len(sys.argv) == 1:
        slot = 1
        HOST = '10.20.34.125'
    if len(sys.argv) == 2:
        slot = int(sys.argv[1])
        HOST = '10.20.34.125'
    if len(sys.argv) == 3:
        slot = int(sys.argv[1])
        HOST = sys.argv[2]
       
    tn = lv_connect(HOST)   
    v = lv_readv(tn,slot)
    print(v)

if __name__ == "__main__":
    main()
