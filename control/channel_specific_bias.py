#!/bin/python3

import sys
import telnetlib
import sqlite3
import datetime
import time

from bias_modification_list import voltage_list, make_list

def channel_specific(arg_detector,arg_half,mod_type):
    
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
        print("please select ./channel_specific_bias.py [outer|inner|both] [east|west|all]")
        sys.exit(1)
                
    giant_voltage_change_list = make_list(mod_type)
    for sector in range(64):
        print("sector: "+str(sector))
        for twr in giant_voltage_change_list[sector]: # loop through dictionaries of all sectors (most are empty)
            set_voltage_offset(hosts,twr["hostid"],twr["board"],twr["tower"],twr["gain"])
        
def read_voltage_offset(channel):
    output_string="$GR"+str(channel)
    return output_string

def voltage_offset(board,tower,gain):
    output_string=str(board)+str(tower)+str(gain)
    return output_string

def get_offset_readings(channel):
    print("Check: "+read_voltage_offset())
    command_string="$GR"+str(channel)
    return command_string

def set_voltage_offset(hosts, host, board, channel, gain_value):
    host_prefix = "10.20.34."
    port_number = "9760"
    if host in hosts:
        print("Yes! "+host+" is in "+str(hosts))
        
        try:
            tn = telnetlib.Telnet(host_prefix+host,port_number)
        except TelnetException as ex:
            print(ex)
            print("cannont connect to controller board @" + host + "...give up.")
            sys.exit()
        command_string = "$GS"
        setting_string = voltage_offset(board,channel,gain_value)
        print("H: "+command_string+setting_string)
        tn.write(b"\n\r")
        tn.write(b"\n\r")

        tn.write(bytes(command_string+setting_string,encoding="ascii"))
        ggg= tn.read_until(b">")
        print(ggg)
        tn.write(b"\n\r")
    
        print("Tower @ ("+board+","+channel+") set to "+gain_value+"\n")
        # for ch in range(8):
            # read_out_string = read_voltage_offset(ch)
            # tn.write(bytes(read_out_string,encoding="ascii"))
            # gg=tn.read_until(b">")
            # print(gg)
            # tn.write(b"\n\r")

                 
if __name__=="__main__":
    print("This script changes the bias voltage channel-by-channel \nand sector-by-sector...it's complicated.")
    if len(sys.argv) == 2:
        print("Usage: channel_specific_bias.py {outer|inner|both} {east|west|all}")
        sys.exit(0)
    arg_det = str(sys.argv[1]).lower()
    arg_half = str(sys.argv[2]).lower()
    host_prefix = "10.20.34."
    port_number = "9760"
    print("debug.0")
    mod_type = "assembly_nominal_vop"
    # mod_type = "common_bias_nominal_vop"
    # mod_type = "led_amplitude_match"
    channel_specific(arg_det, arg_half, mod_type)
