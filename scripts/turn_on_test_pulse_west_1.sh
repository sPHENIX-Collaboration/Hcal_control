#!/bin/sh
for i in $(seq 90 97)
    do 
        board=10.20.34."$i"
        (echo open ${board} 9760
              sleep 1
              echo "\$P0FF"
              sleep 1
              echo "\$P1FF"
              sleep 1
              echo "\$P2FF"
              sleep 1
              echo "\$P3FF"
              sleep 1
              echo "\$P4FF"
              sleep 1
              echo "\$P5FF"
              sleep 1
              echo "\$P6FF"
              sleep 1
              echo "\$P7FF"
              sleep 1
              echo "^[";) | telnet
           
    done
