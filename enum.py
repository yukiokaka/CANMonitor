#!/usr/bin/python3
import os
import select
import sys

def encode_line(line):
    print("RDS000-00000:xxyyzzww")

def enum():
    with open("./test.txt", "r+") as monitor_io:
        timeout = 5
        inputs = [monitor_io]
        
        #polling CANmonitor
        readables, writables, exceptionals = select.select(inputs,[] , [], timeout)
        
        if not (readables or writables or exceptionals):
            print("TIMEOUT! CANMonitor did not respond ", file=sys.stderr)
            exit(1)
        
        #encode data from CANmonitor
        for  f in readables:
            for line in f:
                encode_line(f)
                
                


if __name__ == "__main__":
    enum()




