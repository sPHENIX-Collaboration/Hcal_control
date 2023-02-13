mkdir tower_test

#daq_set_runtype led_tower
#daq_open
#daq_set_max_events 10

for DET in {0..1}
do
    for SEC in {0..31}
    do
        for NS in {0..1}
        do
            for TOW in {0..23}
            do
                python3 one_up_others_down.py $DET $SEC $NS $TOW
                #daq_begin && gtm_startrun
                #gtm_stop && daq_end

                #cp /data/phnxrc/led_tower_by_tower_hcal/led_tower.prdf tower_test/tower_test_${DET}_${SEC}_${NS}_${TOW}.prdf
            done
        done
    done
done
