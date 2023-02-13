#!/bin/env python3

# Oliver Suranyi
# 2022. 12. 06.

import math
from lvcontrol import *

def get_channel_id(channel: str) -> str:
    c = int(channel)
    if c == 0:
        return "00"
    elif c < 5:
        channel_id = 2**(c-1)
        return f"{channel_id:02d}"
    else:
        channel_id = 10*2**(c-5)
        return f"{channel_id:02d}"


slot = input("slot: ")
    
tn = lv_connect('10.20.34.122')
 
while True:
    channel = input("channel: ")
    if channel == "-1":
        break
    lv_enable_single_channel(tn,int(slot),get_channel_id(channel))

lv_disconnect(tn)
