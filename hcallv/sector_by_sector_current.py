#!/bin/env python3:

# Silas Grossberndt
# 2022. 12. 08

#This script allows you to turn on a sector 1 by 1, allows communication with either
#the inner or outer hcal, to switch between must exit the script

#Update--as of 13/12 this script now reads out current of the sector and sends to a file 
import math
from lvcontrol import *

def ch_readi(tn,slot,channel, sector):

    command = '$I'+slot+channel
    tn.write(command.encode('ascii')+b"\n\r")
    x = tn.read_until(b">")
    line = x.decode('ascii')
# delete up to the V01 in above example
# re.DOTALL lets the match traverse \n and \r
#    line = re.sub('^.*?'+command[1:]+'\n\r', '', line, flags=re.DOTALL)
# remove some characters from the string that we don't need    
    line = line.replace('\n\r>', '')
    line = line.replace('\r', '')
    #line = line.replace('A', '')
# split the string into strings of voltages    
    istring = line.split('\n')
# get rid of blanks if they're there
    try:
        istring.remove('')
        istring.remove(' ')
    except ValueError:
        pass
    low_row=2*int(sector)
    low_row=low_row%4
    rs=[low_row, low_row+8, low_row+1, low_row+9]
    fcurrents=[i for i in istring]
    currents=[fcurrents[r] for r in rs] 
    NS=["N", "N", "S", "S"]
    if sector !="off":
       currents_with_sector=["Sector "+sector+NS[i%4]+currents[i]+"\n" for i in range(len(currents))]
   #This prints the currents as associated with the sector number N/S (assuming North is connected
   #the lower number channel) and the current associated with this sector for easy parsing
   # current should only have two elements for single sector, but by doing it this way 
#    print('currents: ',currents)
    return currents_with_sector


def get_sector_id(sector, ioro, tn):
    s=sector
    sl=0
    ch=0
    if ioro=="i":
        sl=8
    elif ioro=="o":
        sl=0
    else:
        print ("not able to discern inner or outer. Closing")
        lv_disconnect(tn)
        quit()
    if s == "off" or s=="OFF" or s=="Off":
        #turns off all channels on all boards to be ready to plug in/out from boards
        sl+=1
        sls=""
        for i in range(8):
            sl+=i
            if sl==10:
                sls="A"
            elif sl==11:
                sls="B"
            elif sl==12:
                sls="C"
            elif sl==13:
                sls="D"
            elif sl==14:
                sls="E"
            elif sl==15:
                sls="F"
            elif sl==16:
                sls="10"
            else:
                sls=str(sl)
            if sls != "10":
                sls = "0"+sls
            #sl = "0"+sl
            print(sls)
            command = '$E'+sls+"00" 
            print(command)
            tn.write(command.encode('ascii')+b"\n\r")
            tn.read_until(b'>')

    elif s=="-1" or s=="exit":
        lv_disconnect(tn)
        quit()
    elif int(s) <= 32:
        si=int(s)
        si_b=si%4
        sl+=int(si/4)+1
        if sl==10:
            sl="A"
        if sl==11:
            sl="B"
        if sl==12:
            sl="C"
        if sl==13:
            sl="D"
        if sl==14:
            sl="E"
        if sl==15:
            sl="F"
        if sl==16:
            sl=10
        sl=str(sl)
        if sl != "10":
            sl = "0"+sl
        if si_b==0:
            ch="03"
        if si_b==1:
            ch="0B"
        if si_b==2:
            ch="25"
        if si_b==3:
            ch="87"
    else:
        print ("couldn't find sector, Closing")
        lv_disconnect(tn)
        quit()
    return sl, ch
innerouter = input("Inner or Outer(i/o): ")
inorout=''
if innerouter=="i":
    inorout="Inner"
if innerouter=="o":
    inorout="Outer"
tn = lv_connect('10.20.34.122')
#the power current for inner or outer hcal is output to file with approptiate name 
with open('power_currents_%s.txt' %inorout,'w') as f: 
    while True:
        sector = input("sector: ")
        if sector == "-1":
            break
        sl, ch=get_sector_id(sector, innerouter, tn)
        if sector != "off" and sector !="OFF" and sector !="Off":
            command = '$E'+sl+ch 
            print(command)
            tn.write(command.encode('ascii')+b"\n\r")
            tn.read_until(b'>')
        current = ch_readi(tn,sl,ch, str(sector))
        for c in current:
            f.write(c)

f.close()
lv_disconnect(tn)
