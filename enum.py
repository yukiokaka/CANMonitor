#!/usr/bin/python3
from canmonitor import Canmonitor
from devicedata import *
import sys


def enum(canmonitor, devicelist = {}):
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
                data_msg, devkind, devindex, data, err_flg = encode_line(line)
                if not(err_flg):
                    print("Deivce:%s, kind = %d, index = %d" %(devicelist[devkind].devicename, devkind, devindex))
                
                


if __name__ == "__main__":
    canmonitor = Canmonitor("./test.txt")
    enum(canmonitor, read_devicedata())




