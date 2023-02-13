#!/bin/python3

def make_list(type):
    if(type=="assembly_nominal_vop"):
        print("Setting each channel to the nominal operating voltage of its SiPMs (based on different sector-by-sector bias settings)")
    elif(type=="led_amplitude_match"):
        print("setting all towers' bias such that their LED-ALL peaks are at the same height over the baseline/pedestal!")        
    elif(type=="common_bias_nominal_vop"):
        print("setting each channel to the nominal operating voltage of its SiPMs (based on a common bias voltage to all sectors)")
    else:
        print("bias_modification_list.py::make_list(type) problem: invalid type of bias control")
        sys.exit(1)
        
    big_list = voltage_list(type)
    return big_list

def voltage_list(type="assebmly_nominal_vop"):
    if(type=="assembly_nominal_vop"):
        voltage_list = [
            # OUTER HCAL
            # Mods:
                # INDEX  # ASBLY # MODS?
                # ----------------------
            [], # HCAL0  # AO-16 # No Mods
            [], # HCAL1  # AO-18 # No Mods
            [], # HCAL2  # AO-20 # No Mods
            [], # HCAL3  # AO-22 # No Mods
            [], # HCAL4  # AO-24 # No Mods
            [], # HCAL5  # AO-26 # No Mods
            [], # HCAL6  # AO-28 # No Mods
            [], # HCAL7  # AO-30 # No Mods
            [], # HCAL8  # AO-32 # No Mods
            [], # HCAL9  # AO-31 # No Mods
            [], # HCAL10 # AO-29 # No Mods
            [], # HCAL11 # AO-27 # No Mods
            [{"hostid":"81","board":"1","tower":"22","gain":"1270"},#south
             {"hostid":"81","board":"1","tower":"23","gain":"1270"},#south
             {"hostid":"81","board":"0","tower":"00","gain":"1270"},#north
             {"hostid":"81","board":"0","tower":"01","gain":"1270"}],#north # HCAL12 # AO-25 # ~ Mods ~
            [], # HCAL13 # AO-23 # No Mods
            [{"hostid":"81","board":"4","tower":"00","gain":"-0090"}, #all north
             {"hostid":"81","board":"4","tower":"01","gain":"-0090"},
             {"hostid":"81","board":"4","tower":"02","gain":"-0090"},
             {"hostid":"81","board":"4","tower":"03","gain":"-0090"},
             {"hostid":"81","board":"4","tower":"04","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"05","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"06","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"07","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"08","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"09","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"10","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"11","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"12","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"13","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"14","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"15","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"16","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"17","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"18","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"19","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"20","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"21","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"22","gain":"-0150"},
             {"hostid":"81","board":"4","tower":"23","gain":"-0150"}], # HCAL14 # AO-21 # ~ Mods ~
            [], # HCAL15 # AO-19 # No Mods
            [], # HCAL16 # AO-17 # No Mods
            [{"hostid":"82","board":"3","tower":"00","gain":"1850"},#S
             {"hostid":"82","board":"3","tower":"01","gain":"1850"},#S
             {"hostid":"82","board":"3","tower":"02","gain":"1270"},#S
             {"hostid":"82","board":"3","tower":"03","gain":"1270"},#S
             {"hostid":"82","board":"3","tower":"04","gain":"1300"},#S
             {"hostid":"82","board":"3","tower":"05","gain":"1300"},#S
             {"hostid":"82","board":"3","tower":"06","gain":"1330"},#S
             {"hostid":"82","board":"3","tower":"07","gain":"1330"},#s
             {"hostid":"82","board":"3","tower":"08","gain":"1390"},#s
             {"hostid":"82","board":"3","tower":"09","gain":"1390"},#s
             {"hostid":"82","board":"3","tower":"10","gain":"1390"},#S
             {"hostid":"82","board":"3","tower":"11","gain":"1390"},#s
             {"hostid":"82","board":"2","tower":"00","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"01","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"02","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"03","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"04","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"05","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"06","gain":"1850"},#n
             {"hostid":"82","board":"2","tower":"07","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"08","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"09","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"10","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"11","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"12","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"13","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"14","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"15","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"16","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"17","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"18","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"19","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"20","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"21","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"22","gain":"1850"},#N
             {"hostid":"82","board":"2","tower":"23","gain":"1850"}],#N # HCAL17 # AO-15 # ~ Mods ~
            [], # HCAL18 # AO-13 # No Mods
            [], # HCAL19 # AO-11 # No Mods
            [], # HCAL20 # AO-9  # No Mods
            [], # HCAL21 # AO-7  # No Mods
            [], # HCAL22 # AO-5  # No Mods
            [], # HCAL23 # AO-3  # No Mods
            [], # HCAL24 # AO-2  # No Mods
            [], # HCAL25 # AO-1  # No Mods
            [], # HCAL26 # AO-4  # No Mods
            [], # HCAL27 # AO-6  # No Mods
            [], # HCAL28 # AO-8  # No Mods
            [], # HCAL29 # AO-10 # No Mods
            [], # HCAL30 # AO-12 # No Mods
            [{"hostid":"91","board":"7","tower":"00","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"01","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"02","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"03","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"04","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"05","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"06","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"07","gain":"0060"},#S
             {"hostid":"91","board":"7","tower":"08","gain":"0030"},#S
             {"hostid":"91","board":"7","tower":"09","gain":"0030"},#S
             {"hostid":"91","board":"7","tower":"10","gain":"0030"},#S
             {"hostid":"91","board":"7","tower":"11","gain":"0030"},#S
             {"hostid":"91","board":"7","tower":"20","gain":"-0090"},#S
             {"hostid":"91","board":"7","tower":"21","gain":"-0090"},#S
             {"hostid":"91","board":"7","tower":"22","gain":"-0090"},#S
             {"hostid":"91","board":"7","tower":"23","gain":"-0090"},#S
             {"hostid":"91","board":"6","tower":"00","gain":"-0060"},#N
             {"hostid":"91","board":"6","tower":"01","gain":"-0060"},#N
             {"hostid":"91","board":"6","tower":"02","gain":"-0060"},#N
             {"hostid":"91","board":"6","tower":"03","gain":"-0060"},#N
             {"hostid":"91","board":"6","tower":"04","gain":"-0030"},#N
             {"hostid":"91","board":"6","tower":"05","gain":"-0030"},#N
             {"hostid":"91","board":"6","tower":"06","gain":"-0030"},#N
             {"hostid":"91","board":"6","tower":"07","gain":"-0030"},#N
             {"hostid":"91","board":"6","tower":"08","gain":"-0030"},#N
             {"hostid":"91","board":"6","tower":"09","gain":"-0030"},#N
             {"hostid":"91","board":"6","tower":"12","gain":"0030"},#N
             {"hostid":"91","board":"6","tower":"13","gain":"0030"},#N
             {"hostid":"91","board":"6","tower":"14","gain":"0030"},#N
             {"hostid":"91","board":"6","tower":"15","gain":"0030"},#N
             {"hostid":"91","board":"6","tower":"16","gain":"0030"},#N
             {"hostid":"91","board":"6","tower":"17","gain":"0030"},#N
             {"hostid":"91","board":"6","tower":"18","gain":"0060"},#N
             {"hostid":"91","board":"6","tower":"19","gain":"0060"},#N
             {"hostid":"91","board":"6","tower":"20","gain":"0060"},#N
             {"hostid":"91","board":"6","tower":"21","gain":"0060"},#N
             {"hostid":"91","board":"6","tower":"22","gain":"0060"},#N
             {"hostid":"91","board":"6","tower":"23","gain":"0060"}], #N # HCAL31 # AO-14 # ~ Mods ~

            # INNER HCAL
            [], # HCAL32 # I-0  # AI-1  # No Mods
            [{"hostid":"96","board":"1","tower":"16","gain":"0820"},#S
             {"hostid":"96","board":"1","tower":"17","gain":"0820"},#S
             {"hostid":"96","board":"1","tower":"18","gain":"0820"},#S
             {"hostid":"96","board":"1","tower":"19","gain":"0820"},#S
             {"hostid":"96","board":"1","tower":"20","gain":"0820"},#S
             {"hostid":"96","board":"1","tower":"21","gain":"0820"},#S
             {"hostid":"96","board":"1","tower":"22","gain":"0820"},#S
             {"hostid":"96","board":"1","tower":"23","gain":"0820"},#S
             {"hostid":"96","board":"0","tower":"00","gain":"0820"},#N
             {"hostid":"96","board":"0","tower":"01","gain":"0820"},#N
             {"hostid":"96","board":"0","tower":"02","gain":"0820"},#N
             {"hostid":"96","board":"0","tower":"03","gain":"0820"},#N
             {"hostid":"96","board":"0","tower":"04","gain":"0820"},#N
             {"hostid":"96","board":"0","tower":"05","gain":"0820"},#N
             {"hostid":"96","board":"0","tower":"06","gain":"0820"},#N
             {"hostid":"96","board":"0","tower":"07","gain":"0820"}],#N, # HCAL33 # I-1  # AI-2  # ~ Mods ~
            [{"hostid":"96","board":"3","tower":"16","gain":"0140"},#S
             {"hostid":"96","board":"3","tower":"17","gain":"0140"},#S
             {"hostid":"96","board":"3","tower":"18","gain":"0140"},#S
             {"hostid":"96","board":"3","tower":"19","gain":"0140"},#S
             {"hostid":"96","board":"3","tower":"20","gain":"0140"},#S
             {"hostid":"96","board":"3","tower":"21","gain":"0140"},#S
             {"hostid":"96","board":"3","tower":"22","gain":"0140"},#S
             {"hostid":"96","board":"3","tower":"23","gain":"0140"},#S
             {"hostid":"96","board":"2","tower":"00","gain":"0140"},#N
             {"hostid":"96","board":"2","tower":"01","gain":"0140"},#N
             {"hostid":"96","board":"2","tower":"02","gain":"0140"},#N
             {"hostid":"96","board":"2","tower":"03","gain":"0140"},#N
             {"hostid":"96","board":"2","tower":"04","gain":"0140"},#N
             {"hostid":"96","board":"2","tower":"05","gain":"0140"},#N
             {"hostid":"96","board":"2","tower":"06","gain":"0140"},#N
             {"hostid":"96","board":"2","tower":"07","gain":"0140"}],#N # HCAL34 # I-2  # AI-4  # ~ Mods ~
            [{"hostid":"96","board":"5","tower":"16","gain":"0140"},#S
             {"hostid":"96","board":"5","tower":"17","gain":"0140"},#S
             {"hostid":"96","board":"5","tower":"18","gain":"0140"},#S
             {"hostid":"96","board":"5","tower":"19","gain":"0140"},#S
             {"hostid":"96","board":"5","tower":"20","gain":"0140"},#S
             {"hostid":"96","board":"5","tower":"21","gain":"0140"},#S
             {"hostid":"96","board":"5","tower":"22","gain":"0140"},#S
             {"hostid":"96","board":"5","tower":"23","gain":"0140"},#S
             {"hostid":"96","board":"4","tower":"00","gain":"0140"},#N
             {"hostid":"96","board":"4","tower":"01","gain":"0140"},#N
             {"hostid":"96","board":"4","tower":"02","gain":"0140"},#N
             {"hostid":"96","board":"4","tower":"03","gain":"0140"},#N
             {"hostid":"96","board":"4","tower":"04","gain":"0140"},#N
             {"hostid":"96","board":"4","tower":"05","gain":"0140"},#N
             {"hostid":"96","board":"4","tower":"06","gain":"0140"},#N
             {"hostid":"96","board":"4","tower":"07","gain":"0140"}],#N # HCAL35 # I-3  # AI-3  # ~ Mods ~
            [{"hostid":"96","board":"7","tower":"16","gain":"0140"},#S
             {"hostid":"96","board":"7","tower":"17","gain":"0140"},#S
             {"hostid":"96","board":"7","tower":"18","gain":"0140"},#S
             {"hostid":"96","board":"7","tower":"19","gain":"0140"},#S
             {"hostid":"96","board":"7","tower":"20","gain":"0140"},#S
             {"hostid":"96","board":"7","tower":"21","gain":"0140"},#S
             {"hostid":"96","board":"7","tower":"22","gain":"0140"},#S
             {"hostid":"96","board":"7","tower":"23","gain":"0140"},#S
             {"hostid":"96","board":"6","tower":"00","gain":"0140"},#N
             {"hostid":"96","board":"6","tower":"01","gain":"0140"},#N
             {"hostid":"96","board":"6","tower":"02","gain":"0140"},#N
             {"hostid":"96","board":"6","tower":"03","gain":"0140"},#N
             {"hostid":"96","board":"6","tower":"04","gain":"0140"},#N
             {"hostid":"96","board":"6","tower":"05","gain":"0140"},#N
             {"hostid":"96","board":"6","tower":"06","gain":"0140"},#N
             {"hostid":"96","board":"6","tower":"07","gain":"0140"}],#N # HCAL36 # I-4  # AI-5  # ~ Mods ~
            [{"hostid":"97","board":"1","tower":"16","gain":"0140"},#S
             {"hostid":"97","board":"1","tower":"17","gain":"0140"},#S
             {"hostid":"97","board":"1","tower":"18","gain":"0140"},#S
             {"hostid":"97","board":"1","tower":"19","gain":"0140"},#S
             {"hostid":"97","board":"1","tower":"20","gain":"0140"},#S
             {"hostid":"97","board":"1","tower":"21","gain":"0140"},#S
             {"hostid":"97","board":"1","tower":"22","gain":"0140"},#S
             {"hostid":"97","board":"1","tower":"23","gain":"0140"},#S
             {"hostid":"97","board":"0","tower":"00","gain":"0140"},#N
             {"hostid":"97","board":"0","tower":"01","gain":"0140"},#N
             {"hostid":"97","board":"0","tower":"02","gain":"0140"},#N
             {"hostid":"97","board":"0","tower":"03","gain":"0140"},#N
             {"hostid":"97","board":"0","tower":"04","gain":"0140"},#N
             {"hostid":"97","board":"0","tower":"05","gain":"0140"},#N
             {"hostid":"97","board":"0","tower":"06","gain":"0140"},#N
             {"hostid":"97","board":"0","tower":"07","gain":"0140"}],#N # HCAL37 # I-5  # AI-6  # ~ Mods ~
            [{"hostid":"97","board":"3","tower":"16","gain":"1200"},#S
             {"hostid":"97","board":"3","tower":"17","gain":"1200"},#S
             {"hostid":"97","board":"3","tower":"18","gain":"1200"},#S
             {"hostid":"97","board":"3","tower":"19","gain":"1200"},#S
             {"hostid":"97","board":"3","tower":"20","gain":"1200"},#S
             {"hostid":"97","board":"3","tower":"21","gain":"1200"},#S
             {"hostid":"97","board":"3","tower":"22","gain":"1200"},#S
             {"hostid":"97","board":"3","tower":"23","gain":"1200"},#S
             {"hostid":"97","board":"2","tower":"00","gain":"1790"},#N
             {"hostid":"97","board":"2","tower":"01","gain":"1790"},#N
             {"hostid":"97","board":"2","tower":"02","gain":"1790"},#N
             {"hostid":"97","board":"2","tower":"03","gain":"1790"},#N
             {"hostid":"97","board":"2","tower":"04","gain":"1790"},#N
             {"hostid":"97","board":"2","tower":"05","gain":"1790"},#N
             {"hostid":"97","board":"2","tower":"06","gain":"1790"},#N
             {"hostid":"97","board":"2","tower":"07","gain":"1790"}],#N # HCAL38 # I-6  # AI-7  # ~ Mods ~
            [{"hostid":"97","board":"5","tower":"16","gain":"0820"},#S
             {"hostid":"97","board":"5","tower":"17","gain":"0820"},#S
             {"hostid":"97","board":"5","tower":"18","gain":"0820"},#S
             {"hostid":"97","board":"5","tower":"19","gain":"0820"},#S
             {"hostid":"97","board":"5","tower":"20","gain":"0820"},#S
             {"hostid":"97","board":"5","tower":"21","gain":"0820"},#S
             {"hostid":"97","board":"5","tower":"22","gain":"0820"},#S
             {"hostid":"97","board":"5","tower":"23","gain":"0820"},#S
             {"hostid":"97","board":"4","tower":"00","gain":"0820"},#N
             {"hostid":"97","board":"4","tower":"01","gain":"0820"},#N
             {"hostid":"97","board":"4","tower":"02","gain":"0820"},#N
             {"hostid":"97","board":"4","tower":"03","gain":"0820"},#N
             {"hostid":"97","board":"4","tower":"04","gain":"0820"},#N
             {"hostid":"97","board":"4","tower":"05","gain":"0820"},#N
             {"hostid":"97","board":"4","tower":"06","gain":"0820"},#N
             {"hostid":"97","board":"4","tower":"07","gain":"0820"}],#N # HCAL39 # I-7  # AI-8  # ~ Mods ~
            [{"hostid":"97","board":"7","tower":"16","gain":"0910"},#S
             {"hostid":"97","board":"7","tower":"17","gain":"0910"},#S
             {"hostid":"97","board":"7","tower":"18","gain":"0910"},#S
             {"hostid":"97","board":"7","tower":"19","gain":"0910"},#S
             {"hostid":"97","board":"7","tower":"20","gain":"0910"},#S
             {"hostid":"97","board":"7","tower":"21","gain":"0910"},#S
             {"hostid":"97","board":"7","tower":"22","gain":"0910"},#S
             {"hostid":"97","board":"7","tower":"23","gain":"0910"},#S
             {"hostid":"97","board":"6","tower":"00","gain":"0910"},#N
             {"hostid":"97","board":"6","tower":"01","gain":"0910"},#N
             {"hostid":"97","board":"6","tower":"02","gain":"0910"},#N
             {"hostid":"97","board":"6","tower":"03","gain":"0910"},#N
             {"hostid":"97","board":"6","tower":"04","gain":"0910"},#N
             {"hostid":"97","board":"6","tower":"05","gain":"0910"},#N
             {"hostid":"97","board":"6","tower":"06","gain":"0910"},#N
             {"hostid":"97","board":"6","tower":"07","gain":"0910"}],#N # HCAL40 # I-8  # AI-9  # ~ Mods ~
            [{"hostid":"84","board":"1","tower":"16","gain":"0910"},#S
             {"hostid":"84","board":"1","tower":"17","gain":"0910"},#S
             {"hostid":"84","board":"1","tower":"18","gain":"0910"},#S
             {"hostid":"84","board":"1","tower":"19","gain":"0910"},#S
             {"hostid":"84","board":"1","tower":"20","gain":"0910"},#S
             {"hostid":"84","board":"1","tower":"21","gain":"0910"},#S
             {"hostid":"84","board":"1","tower":"22","gain":"0910"},#S
             {"hostid":"84","board":"1","tower":"23","gain":"0910"},#S
             {"hostid":"84","board":"0","tower":"00","gain":"0910"},#N
             {"hostid":"84","board":"0","tower":"01","gain":"0910"},#N
             {"hostid":"84","board":"0","tower":"02","gain":"0910"},#N
             {"hostid":"84","board":"0","tower":"03","gain":"0910"},#N
             {"hostid":"84","board":"0","tower":"04","gain":"0910"},#N
             {"hostid":"84","board":"0","tower":"05","gain":"0910"},#N
             {"hostid":"84","board":"0","tower":"06","gain":"0910"},#N
             {"hostid":"84","board":"0","tower":"07","gain":"0910"}],#N # HCAL41 # I-9  # AI-10 # ~ Mods ~
            [], # HCAL42 # I-10 # AI-11 # No Mods
            [], # HCAL43 # I-11 # AI-12 # No Mods
            [], # HCAL44 # I-12 # AI-13 # No Mods
            [], # HCAL45 # I-13 # AI-14 # No Mods
            [], # HCAL46 # I-14 # AI-15 # No Mods
            [], # HCAL47 # I-15 # AI-16 # No Mods
            [], # HCAL48 # I-16 # AI-17 # No Mods
            [], # HCAL49 # I-17 # AI-18 # No Mods
            [], # HCAL50 # I-18 # AI-19 # No Mods
            [], # HCAL51 # I-19 # AI-20 # No Mods
            [], # HCAL52 # I-20 # AI-21 # No Mods
            [], # HCAL53 # I-21 # AI-22 # No Mods
            [], # HCAL54 # I-22 # AI-23 # No Mods
            [], # HCAL55 # I-23 # AI-24 # No Mods
            [], # HCAL56 # I-24 # AI-25 # No Mods
            [], # HCAL57 # I-25 # AI-26 # No Mods
            [], # HCAL58 # I-26 # AI-27 # No Mods
            [], # HCAL59 # I-27 # AI-28 # No Mods
            [], # HCAL60 # I-28 # AI-29 # No Mods
            [], # HCAL61 # I-29 # AI-30 # No Mods
            [], # HCAL62 # I-30 # AI-31 # No Mods
            []  # HCAL63 # I-31 # AI-32 # No Mods
        ]
    elif(type=="led_amplitude_match"):
        voltage_list = [
            # OUTER HCAL
            # Mods:
                # INDEX  # ASBLY # MODS?
                # ----------------------
            [], # HCAL0  # AO-16 
            [], # HCAL1  # AO-18 
            [], # HCAL2  # AO-20 
            [], # HCAL3  # AO-22 
            [], # HCAL4  # AO-24 
            [], # HCAL5  # AO-26 
            [], # HCAL6  # AO-28 
            [], # HCAL7  # AO-30 
            [], # HCAL8  # AO-32 
            [], # HCAL9  # AO-31 
            [], # HCAL10 # AO-29 
            [], # HCAL11 # AO-27 
            [], # HCAL12 # AO-25 
            [], # HCAL13 # AO-23 
            [], # HCAL14 # AO-21 
            [], # HCAL15 # AO-19 
            [], # HCAL16 # AO-17 
            [], # HCAL17 # AO-15 
            [], # HCAL18 # AO-13
            [], # HCAL19 # AO-11
            [], # HCAL20 # AO-9 
            [], # HCAL21 # AO-7 
            [], # HCAL22 # AO-5 
            [], # HCAL23 # AO-3 
            [], # HCAL24 # AO-2 
            [], # HCAL25 # AO-1 
            [], # HCAL26 # AO-4 
            [], # HCAL27 # AO-6 
            [], # HCAL28 # AO-8 
            [], # HCAL29 # AO-10
            [], # HCAL30 # AO-12
            [], # HCAL31 # AO-14

            # INNER HCAL
            [], # HCAL32 # I-0  # AI-1 
            [], # HCAL33 # I-1  # AI-2 
            [], # HCAL34 # I-2  # AI-4 
            [], # HCAL35 # I-3  # AI-3 
            [], # HCAL36 # I-4  # AI-5 
            [], # HCAL37 # I-5  # AI-6 
            [], # HCAL38 # I-6  # AI-7 
            [], # HCAL39 # I-7  # AI-8 
            [], # HCAL40 # I-8  # AI-9 
            [], # HCAL41 # I-9  # AI-10
            [], # HCAL42 # I-10 # AI-11 
            [], # HCAL43 # I-11 # AI-12 
            [], # HCAL44 # I-12 # AI-13 
            [], # HCAL45 # I-13 # AI-14 
            [], # HCAL46 # I-14 # AI-15 
            [], # HCAL47 # I-15 # AI-16 
            [], # HCAL48 # I-16 # AI-17 
            [], # HCAL49 # I-17 # AI-18 
            [], # HCAL50 # I-18 # AI-19 
            [], # HCAL51 # I-19 # AI-20 
            [], # HCAL52 # I-20 # AI-21 
            [], # HCAL53 # I-21 # AI-22 
            [], # HCAL54 # I-22 # AI-23 
            [], # HCAL55 # I-23 # AI-24 
            [], # HCAL56 # I-24 # AI-25 
            [], # HCAL57 # I-25 # AI-26 
            [], # HCAL58 # I-26 # AI-27 
            [], # HCAL59 # I-27 # AI-28 
            [], # HCAL60 # I-28 # AI-29 
            [], # HCAL61 # I-29 # AI-30 
            [], # HCAL62 # I-30 # AI-31 
            []  # HCAL63 # I-31 # AI-32 
        ]
    elif (type=="common_bias_nominal_vop"):
        voltage_list = [
            # OUTER HCAL
            # Mods:
                # INDEX  # ASBLY # MODS?
                # ----------------------
            [], # HCAL0  # AO-16 
            [], # HCAL1  # AO-18 
            [], # HCAL2  # AO-20 
            [], # HCAL3  # AO-22 
            [], # HCAL4  # AO-24 
            [], # HCAL5  # AO-26 
            [], # HCAL6  # AO-28 
            [], # HCAL7  # AO-30 
            [], # HCAL8  # AO-32 
            [], # HCAL9  # AO-31 
            [], # HCAL10 # AO-29 
            [], # HCAL11 # AO-27 
            [], # HCAL12 # AO-25 
            [], # HCAL13 # AO-23 
            [], # HCAL14 # AO-21 
            [], # HCAL15 # AO-19 
            [], # HCAL16 # AO-17 
            [], # HCAL17 # AO-15 
            [], # HCAL18 # AO-13
            [], # HCAL19 # AO-11
            [], # HCAL20 # AO-9 
            [], # HCAL21 # AO-7 
            [], # HCAL22 # AO-5 
            [], # HCAL23 # AO-3 
            [], # HCAL24 # AO-2 
            [], # HCAL25 # AO-1 
            [], # HCAL26 # AO-4 
            [], # HCAL27 # AO-6 
            [], # HCAL28 # AO-8 
            [], # HCAL29 # AO-10
            [], # HCAL30 # AO-12
            [], # HCAL31 # AO-14

            # INNER HCAL
            [], # HCAL32 # I-0  # AI-1 
            [], # HCAL33 # I-1  # AI-2 
            [], # HCAL34 # I-2  # AI-4 
            [], # HCAL35 # I-3  # AI-3 
            [], # HCAL36 # I-4  # AI-5 
            [], # HCAL37 # I-5  # AI-6 
            [], # HCAL38 # I-6  # AI-7 
            [], # HCAL39 # I-7  # AI-8 
            [], # HCAL40 # I-8  # AI-9 
            [], # HCAL41 # I-9  # AI-10
            [], # HCAL42 # I-10 # AI-11 
            [], # HCAL43 # I-11 # AI-12 
            [], # HCAL44 # I-12 # AI-13 
            [], # HCAL45 # I-13 # AI-14 
            [], # HCAL46 # I-14 # AI-15 
            [], # HCAL47 # I-15 # AI-16 
            [], # HCAL48 # I-16 # AI-17 
            [], # HCAL49 # I-17 # AI-18 
            [], # HCAL50 # I-18 # AI-19 
            [], # HCAL51 # I-19 # AI-20 
            [], # HCAL52 # I-20 # AI-21 
            [], # HCAL53 # I-21 # AI-22 
            [], # HCAL54 # I-22 # AI-23 
            [], # HCAL55 # I-23 # AI-24 
            [], # HCAL56 # I-24 # AI-25 
            [], # HCAL57 # I-25 # AI-26 
            [], # HCAL58 # I-26 # AI-27 
            [], # HCAL59 # I-27 # AI-28 
            [], # HCAL60 # I-28 # AI-29 
            [], # HCAL61 # I-29 # AI-30 
            [], # HCAL62 # I-30 # AI-31 
            []  # HCAL63 # I-31 # AI-32 
        ]
    else:
        voltage_list = [[]]
    return voltage_list

if __name__=="__main__":
    type = "assembly_nominal_vop"
    # type = "common_bias_nominal_vop"
    # type = "led_amplitude_match"
    print("Making channel-by-channel bias-modification list: "+type)
    voltage_list(type)
