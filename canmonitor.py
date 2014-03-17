import os
import select
import sys


class Canmonitor(object):

    def __init__(self, devicename = "./canmonitor"):
        print("CANMonitor instance is made")
        self.devicename = devicename
        
    def __enter__(self):
        print("Open CANMonitor")
        self.f = open(self.devicename, "a+")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Close CANMonitor")
        self.f.close()

    def polling(self, inputs = [], outputs = [], timeout = 5):
        if not(inputs):
            inputs.append(self.f)

        #polling CANmonitor
        readables, writables, exceptionals = select.select(inputs, outputs, [], timeout)
        
        if not (readables or writables or exceptionals):
            print("CANMONITOR TIMEOUT!", file = sys.stderr)
            exit(1)
            
        return readables

    
