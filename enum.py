#!/usr/bin/python3
from canmonitor import Canmonitor
from devicedata import *
import sys
from subprocess import Popen, PIPE
import struct


def enum(canmonitor, devicelist = {}):
    with  canmonitor:
        canmonitor.f.stdout.flush()

        canmonitor.f.stdin.write(b"F")
        canmonitor.f.stdin.write(b"WDS181-00000:")
        canmonitor.f.stdin.write(b"F")
        canmonitor.f.stdin.flush()
        print("waiting for response", file = sys.stderr)

                
        resultlist= "".join([chr(i) for i in canmonitor.f.stdout.read(10000)])
        for i in resultlist.split("\n"):
            if i.lstrip("\n") != "":
                data_msg, devkind, devindex, data, err_flg = encode_line(i.lstrip("\n"))
                print("Deivce:%s, kind = %d, index = %d" %(devicelist[devkind].devicename, devkind, devindex))




if __name__ == "__main__":
    canmonitor = Canmonitor("/home/yuki/robotech/svn/circuit/misc/hidaka/pcprogram/canmonitor_sample/canmonitorio")
    enum(canmonitor, read_devicedata())




