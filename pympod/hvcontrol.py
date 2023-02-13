#!/bin/env python3
import subprocess
import re

ip_default = '10.20.34.148'

def mainframe_status( ip = ip_default ):
    getter = ['snmpget',
    '-Oqv',
    '-v',
    '2c',
    '-M',
    '+/home/phnxrc/haggerty/MIBS', 
    '-m', 
    '+WIENER-CRATE-MIB', 
    '-c', 
    'public', 
    ip,
    'sysMainSwitch.0']

    answer = subprocess.run(getter,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    if str(answer.stdout[0:2]) == "on":
        return 1
    else:
        return 0


def mainframe_on_off( on_off, ip = ip_default ):
    on_off_int = int(on_off == "on")
    
    setter = ['snmpset', 
    '-Oqv', 
    '-v', 
    '2c',
    '-M', 
    '+/home/phnxrc/haggerty/MIBS', 
    '-m', 
    '+WIENER-CRATE-MIB', 
    '-c', 
    'guru', 
    ip,
    'sysMainSwitch.0',
    'i',
    str(on_off_int)]

    print(setter)
    answer = subprocess.run(setter, 
    universal_newlines=True, 
             stdout=subprocess.PIPE, 
             stderr=subprocess.PIPE)

    print(answer.stderr)


def channel_status( slot = 0, channel = 0, ip = ip_default ): 
    
    getter = ['snmpget', 
   '-OqvU', 
   '-v', 
   '2c', 
   '-M', 
   '+/home/phnxrc/haggerty/MIBS', 
   '-m', 
   '+WIENER-CRATE-MIB', 
   '-c', 
   'public', 
   ip,
   'outputSwitch.u0']
    getter[-2] = ip

    channel_id = slot*100 + channel
    getter[-1] = 'outputSwitch.u'+str(channel_id)
#    print(getter)
    answer = subprocess.run(getter, 
            universal_newlines=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)
   
    if str(answer.stdout[0:2]) == "on":
        return 1
    else:
        return 0


 
# 
def readmodule(  what = 'outputMeasurementVoltage', slot = 0, ip = ip_default ): 

    nchmod = 8
    getter = ['snmpget', 
   '-OqvU', 
   '-v', 
   '2c', 
   '-M', 
   '+/home/phnxrc/haggerty/MIBS', 
   '-m', 
   '+WIENER-CRATE-MIB', 
   '-c', 
   'public', 
   ip,
   'outputMeasurementSenseVoltage.u0']
    getter[-2] = ip

    readback = []
    for channel in range(nchmod):
        channel_id = slot*100 + channel
        getter[-1] = what+'.u'+str(channel_id)
        print(getter)
        answer = subprocess.run(getter, 
                universal_newlines=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)


        x = re.findall('\d*\.?\d+',answer.stdout)
        rb = x #float(x[0])
#        print(rb)
        readback.append(rb)

#    print(readback)
    return readback


def readchannel(  what = 'outputMeasurementVoltage', slot = 0, channel = 0, ip = ip_default ): 
    
    getter = ['snmpget', 
   '-OqvU', 
   '-v', 
   '2c', 
   '-M', 
   '+/home/phnxrc/haggerty/MIBS', 
   '-m', 
   '+WIENER-CRATE-MIB', 
   '-c', 
   'public', 
   ip,
   'outputMeasurementSenseVoltage.u0']
    getter[-2] = ip

    channel_id = slot*100 + channel
    getter[-1] = what+'.u'+str(channel_id)
#    print(getter)
    answer = subprocess.run(getter, 
            universal_newlines=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)
   
    #print(answer)
    #print("***********************")
    #print(answer.stdout)

    x = re.findall('\d*\.?\d+',answer.stdout)
       
    if not x:
        return 0.0

    rb = float(x[0])
#    print(rb)

    #return answer
    return rb

def writechannel(  what = 'outputVoltage', 
    slot = 0, channel = 0, 
    type = 'F', value = 0.0, 
    ip = ip_default ): 

    setter = ['snmpset', 
   '-Oqv',
   '-v', 
   '2c', 
   '-M', 
   '+/home/phnxrc/haggerty/MIBS', 
   '-m', 
   '+WIENER-CRATE-MIB', 
   '-c', 
   'guru', 
   ip,
   'ouputVoltage.u0',
   'F',
   '0.0']
    
    setter[-1] = str(value)
    setter[-2] = type
    setter[-3] = what
    setter[-4] = ip

    channel_id = slot*100 + channel
    setter[-3] = what+'.u'+str(channel_id)
    print(setter)
    answer = subprocess.run(setter, 
             universal_newlines=True, 
             stdout=subprocess.PIPE, 
             stderr=subprocess.PIPE)
    
    #print(answer.stdout)
    x = re.findall('\d*\.?\d+',answer.stdout)

    if not x:
        return ""

    rb = float(x[0])
    #print(rb)
    return rb

def main():

    what = 'outputVoltage'
    print(what)
    response = writechannel(what,0,0,'F',66.0)
    print(response)

    module = readmodule(what, 0) 
    print(module)
    
    channel = readchannel(what,0,0)
    print(channel)

if __name__ == "__main__":
    main()
