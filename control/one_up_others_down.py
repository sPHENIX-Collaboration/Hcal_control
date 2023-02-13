import sys
import re
from channel_specific_bias import set_voltage_offset

hosts_outer_east = ["80","81","82","83"]
hosts_outer_west = ["90","91","92","93"]
hosts_inner_east = ["84","85","86","87"]
hosts_inner_west = ["94","95","96","97"]

hosts = hosts_outer_east + hosts_outer_west + hosts_inner_east + hosts_inner_west

sector_host_map = {
    "OHCal0": "92",
    "OHCal1": "92",
    "OHCal2": "92",
    "OHCal3": "92",

    "OHCal4": "93",
    "OHCal5": "93",
    "OHCal6": "93",
    "OHCal7": "93",

    "OHCal8": "80",
    "OHCal9": "80",
    "OHCal10": "80",
    "OHCal11": "80",

    "OHCal12": "81",
    "OHCal13": "81",
    "OHCal14": "81",
    "OHCal15": "81",

    "OHCal16": "82",
    "OHCal17": "82",
    "OHCal18": "82",
    "OHCal19": "82",

    "OHCal20": "83",
    "OHCal21": "83",
    "OHCal22": "83",
    "OHCal23": "83",

    "OHCal24": "90",
    "OHCal25": "90",
    "OHCal26": "90",
    "OHCal27": "90",

    "OHCal28": "91",
    "OHCal29": "91",
    "OHCal30": "91",
    "OHCal31": "91",


    "IHCal0": "96",
    "IHCal1": "96",
    "IHCal2": "96",
    "IHCal3": "96",

    "IHCal4": "97",
    "IHCal5": "97",
    "IHCal6": "97",
    "IHCal7": "97",

    "IHCal8": "84",
    "IHCal9": "84",
    "IHCal10": "84",
    "IHCal11": "84",

    "IHCal12": "85",
    "IHCal13": "85",
    "IHCal14": "85",
    "IHCal15": "85",

    "IHCal16": "86",
    "IHCal17": "86",
    "IHCal18": "86",
    "IHCal19": "86",

    "IHCal20": "87",
    "IHCal21": "87",
    "IHCal22": "87",
    "IHCal23": "87",

    "IHCal24": "94",
    "IHCal25": "94",
    "IHCal26": "94",
    "IHCal27": "94",

    "IHCal28": "95",
    "IHCal29": "95",
    "IHCal30": "95",
    "IHCal31": "95",

}


def increase_one_voltage(sector, north_south, tower):
    global host

    gain_modification = 0

    for sec in sector_host_map.keys():
        host = sector_host_map[sec]
        sector_number = int(re.findall(r'\d+',sec)[0])
        print(sector_number)

        for ns in range(2):
            board = (sector_number % 4)*2 + ns

            for tow in range(24):
                if sector == sec and north_south == ns and tower == tow:
                    gain_modification = 2499
                else:
                    gain_modification = -2499
                 
                set_voltage_offset(hosts, host, board, tow, gain_modification)


def main(argv):

    detector = ""
    if argv[1] == 1:
        detector = "IHCal"
    else:
        detector = "OHCal"

    sector = detector+argv[2]
    north_south = argv[3]
    tower = argv[4]

    increase_one_voltage(sector,north_south,tower)

if __name__ == "__main__":
   main(sys.argv)
