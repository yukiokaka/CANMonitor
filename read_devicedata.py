import glob

def read_devicedata():
    files = glob.glob("./*.py")
    for file in files:
        with open(file, "r") as f:
             for line in f:
                 print(line.rstrip())


if __name__ == "__main__":
    read_devicedata()
