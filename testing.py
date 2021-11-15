import glob
import serial
import time

from pd9530 import PD9530

def barcode_reader():

    ports = glob.glob('/dev/ttyACM[0-9]*')
    print(ports[0])
    #fp = open(ports[0], 'rb')

    scanner = PD9530(ports[0])
    scanner.attach()

    for code in scanner.readlines():
        print(code)

    scanner.close()

if __name__ == '__main__':
    try:
        while True:
            barcode_reader()

    except KeyboardInterrupt:
        pass