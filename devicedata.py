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
                self.cmd[row[2].lstrip()] = row[1].lstrip()
                


    def printdata(self):
        print("devicename = %s, %s, devicekind = %d" %(self.devicename, self.std_or_ext, self.devicekind_id))
        print("==CMD List==")
        for cmd_name, cmd_id in self.cmd.items(): 
            print(cmd_name, ":", cmd_id)
        print("============")


def read_devicedata():
    devicelist = {}
    files = glob.glob("devicelist/*.csv")
    
    for file in files:
        with open(file, "r") as f:
            read_data = csv.reader(f)
            new_device = Devicedata(read_data)
            devicelist[new_device.devicekind_id] = new_device
    for i, data in devicelist.items():
        data.printdata()
        
    return devicelist


def encode_line(line):
    msg_id = ""
    data_msg = ""
    devkind = 0
    devindex = 0
    data = ""
    err_flg = 0
    if line[0] == "R":
        data_msg = line[1]
        ext_id_msg = line[2]
        if ext_id_msg == "S":
            msg_id = int(line[3:6], 16)
            devkind = (msg_id & 0x70) >> 4
            devindex = msg_id & 0xF
          
        elif ext_id_msg == "E":
            msg_id = int(line[3:6] + line[7:12], 16)
            devkind = (msg_id & 0xFF00) >> 8
            devindex = (msg_id & 0xFF)

        data = line[13:]
    else:
        err_flg = 1
        
    return data_msg, devkind, devindex, data, err_flg

if __name__ == "__main__":
    devicelist = read_devicedata()
    data_msg, devkind, devindex, data = encode_line("RDE001-00001:xxyyzzww")
    print("Deivce:%s, kind = %d, index = %d" %(devicelist[devkind].devicename, devkind, devindex))
