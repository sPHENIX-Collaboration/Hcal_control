#!/bin/env python3

# John Haggerty, BNL
# 2021.03.10

import justpy as jp
import pandas as pd
import time
import asyncio
from lvcontrol import *

controller_ip = '10.20.34.126'
nslots = 15

def button_click(self,msg):
#    print(self.slot,self.onoff)
    tn = lv_connect(controller_ip)
    lv_enable(tn,self.slot,self.onoff)
    lv_disconnect(tn)

chnames = ['Slot', 'Channel 0', 'Channel 1', 'Channel 2', 'Channel 3', 'Channel 4', 'Channel 5', 
                  'Channel 6', 'Channel 7', 'Channel 8', 'Channel 9', 'Supply']

wp = jp.WebPage(delete_flag=False)
wp.title = 'TPC LV'

header_div = jp.Div(text='TPC Slice Test LV', a=wp, classes = 'text-5xl text-white bg-blue-500 hover:bg-blue-700 m-1')
time_div = jp.Div(a=wp, classes = 'text-1xl text-white bg-blue-500 hover:bg-blue-700 m-1')
the_time = jp.P(a=time_div)
on_button_div = jp.Div(a=wp)
off_button_div = jp.Div(a=wp)
button_classes = 'w-16 mr-2 mb-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full'

for i in range(nslots):
        b = jp.Button(text=f'ON {i+1}', a=on_button_div, classes=button_classes, click=button_click)
        b.slot = i+1
        b.onoff = 1

for i in range(nslots):
        b = jp.Button(text=f'OFF {i+1}', a=off_button_div, classes=button_classes, click=button_click)
        b.slot = i+1
        b.onoff = 0

data_div = jp.Div(a=wp)
gridv = jp.AgGrid(a=data_div)
gridv.options.pagination = True
gridv.options.paginationAutoPageSize = True

async def voltages():
    while True:
        the_time.text = time.strftime("%a, %d %b %Y, %H:%M:%S", time.localtime())
        all_readings = []
        tn = lv_connect(controller_ip)
        for i in range(nslots):
            voltages = lv_readv(tn,i+1)
#            print('Voltages Slot: ',i+1,voltages)
            voltages.insert(0,'V'+str(i+1))
            all_readings.append(voltages)

            currents = lv_readi(tn,i+1)
            total_current = sum(currents)
#            print('Currents Slot: ',i+1,currents)
            currents.append(total_current)
            currents.insert(0,'I'+str(i+1))
            all_readings.append(currents)

        lv_disconnect(tn)

        dfreadings = pd.DataFrame(all_readings,columns=chnames)
        dfreadings.round(4)
#        print(dfreadings)
        gridv.load_pandas_frame(dfreadings)
        jp.run_task(wp.update())
        await asyncio.sleep(2)

async def voltages_init():
    jp.run_task(voltages())

async def voltages_test():
    return wp

jp.justpy(voltages_test, startup=voltages_init)
