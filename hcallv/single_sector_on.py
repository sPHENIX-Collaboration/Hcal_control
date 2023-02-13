#!/bin/env python3

# Oliver Suranyi
# 2022. 12. 06.

import math
from lvcontrol import *

def get_slot_id(det, sector):
    if det == "O":
        return sector // 4 + 1
    elif det == "I":
        return sector // 4 + 9

def get_binary_code(sector):
    binary_code = ["0","0","0","0","0","0","0","0"]
    i = (sector % 4) * 2
    binary_code[i] = "1"
    binary_code[i+1] = "1"
    return ''.join(binary_code)

def get_hex_code(binary_code):
    binary_code = binary_code[::-1]
    hex_code = hex((int(binary_code,2))).split("x")[1]
    if len(hex_code) == 1:
        hex_code = "0"+hex_code
    return hex_code

tn = lv_connect('10.20.34.122')
 
read = ""
slot = None

while True:
    read = input("sector: ")
    if read == "-1":
        #lv_reset(tn)
        break
    elif read == "status":
        status_report(tn)
    else:
        if slot:
            lv_enable(tn,slot,0)
            time.sleep(1)
    
        det, sector = read.split("-")
        sector = int(sector)
        slot = get_slot_id(det, sector)
        binary_code = get_binary_code(sector)
        hex_code = get_hex_code(binary_code)
        lv_enable_combined_channels(tn,int(slot),hex_code) 

lv_disconnect(tn)
