#!/usr/bin/python3

import glob
import csv

class Devicedata():
    def __init__(self, csv_data):
        self.devicename = ""
        self.std_or_ext = "standard"
        self.devicekind_id = 0x00
        self.cmd = {}
        for row in csv_data:
            if   row[0] == "devicename": 
                self.devicename = row[1]
            elif row[0] == "standard" or  row[0] == "extend":
                self.std_or_ext =  row[0]
                self.devicekind_id = int(row[1], 16)
            elif row[0] == "cmd":
                self.cmd[row[2]] = row[1]
                


    def printdata(self):
        print("devicename = %s, %s, devicekind = %d" %(self.devicename, self.std_or_ext, self.devicekind_id))
        print("CMD= ", self.cmd)


def read_devicedata():
    devicelist = []
    files = glob.glob("devicelist/*.csv")
    for file in files:
        with open(file, "r") as f:
            read_data = csv.reader(f)
            devicelist.append(Devicedata(read_data))
    
    for i in devicelist:
        i.printdata()

    return devicelist

if __name__ == "__main__":
    read_devicedata()
