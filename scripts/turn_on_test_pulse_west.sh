#!/bin/sh
for i in $(seq 90 97)
    do 
        board=10.20.34."$i "9760
        telnet $board
          {
              echo "\$"P0FF;
              echo "\$"P1FF;
              echo "\$"P2FF;
              echo "\$"P3FF;
              echo "\$"P4FF;
              echo "\$"P5FF;
              echo "\$"P6FF;
              echo "\$"P7FF;
              echo "^[";
           }
    done
