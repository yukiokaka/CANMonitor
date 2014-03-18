import os
import select
import sys
from subprocess import Popen, PIPE, STDOUT

class Canmonitor(object):

    def __init__(self, devicename = "./canmonitor"):
        print("CANMonitor instance is made")
        self.devicename = devicename

    def __enter__(self):
        print("Open CANMonitor")
        self.f = Popen(self.devicename, stdin=PIPE, stdout=PIPE)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Close CANMonitor")
        self.f.stdin.close()
        self.f.stdout.close()

    def polling(self, inputs = [], outputs = [], timeout = 2):
        if not(inputs):
            inputs.append(self.f.stdin)
        if not(outputs):
            outputs.append(self.f.stdout)
        #polling CANmonitor
        readables, writables, exceptionals = select.select(inputs, outputs, [], timeout)

        if not (readables or writables or exceptionals):
            print("CANMONITOR TIMEOUT!", file = sys.stderr)
            exit(1)

        return readables


