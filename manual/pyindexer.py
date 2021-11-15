import serial.tools.list_ports as port_list
import csv
from pd9530 import PD9530

ports = list(port_list.comports())

for port in ports:
    print(port)


def write_in_file(data):
    c_split = data.split("-")
    c_cap_raw = c_split[-1]
    c_cap = c_cap_raw[1:].rstrip()

    with open("Cells.csv", 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([c_cap])

def barcode_reader():

    #ports = glob.glob('/dev/ttyACM[0-9]*')
    #print(ports[0])
    #fp = open(ports[0], 'rb')



    for port, desc, hwid in sorted(ports):
        #print("{}: {} [{}]".format(port, desc, hwid))

        scanner = PD9530(port)
        scanner.attach()

    # scanner = PD9530("COM6")
    # scanner.attach()

    for code in scanner.readlines():
        # check_cell(code)
        write_in_file(code)
        print(code)

    scanner.close()


if __name__ == '__main__':
    try:
        while True:
            barcode_reader()

    except KeyboardInterrupt:
        pass