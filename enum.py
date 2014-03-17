#!/usr/bin/python3
from canmonitor import Canmonitor
import sys


def encode_line(line):
    print(line)


def enum(canmonitor):
    with  canmonitor:
        canmonitor.f.write("F")
        canmonitor.f.write("WDS181-00000:")
        canmonitor.f.write("F")
        canmonitor.f.flush()
        
        #This seek is test code, beacause test is executed using txt file
        canmonitor.f.seek(0)
        #--------------------------------------------------------------#

        print("waiting for response", file = sys.stderr)

        readables = canmonitor.polling()
        
        #encode data from CANmonitor
        for f in readables:
            for line in f:
                encode_line(line.rstrip())
                
                


if __name__ == "__main__":
    canmonitor = Canmonitor("./test.txt")
    enum(canmonitor)




