#!/bin/env python3

# Oliver Suranyi
# 2022. 12. 06.

import math
from lvcontrol import *
   
tn = lv_connect('10.20.34.122')
 
while True:
    slot = input("slot: ")
    setting = input("setting: ")
    if setting == "-1":
        break
    elif setting == "status":
        status_report(tn)
        continue

    setting = setting[::-1]
    setting_hex = hex((int(setting,2)))
    
    setting_hex = setting_hex.split("x")[1]

    if len(setting_hex) == 1:
        lv_enable_combined_channels(tn,int(slot),"0"+setting_hex)
    elif len(setting_hex) == 2:
        lv_enable_combined_channels(tn,int(slot),setting_hex)
    else:
        break

lv_disconnect(tn)
