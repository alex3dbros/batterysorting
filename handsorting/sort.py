import serial.tools.list_ports as port_list
from pd9530 import PD9530

ports = list(port_list.comports())

# for port in ports:
#     print(port)



ranges = {"Trash":"0-999", "1000":"1000-1499", "1500": "1500-1999", "2000":"2000-2199", "2200": "2200-2399",
          "2400": "2400-2599", "2600":"2600-2799", "2800":"2800-2999", "3000": "3000-3500"}


def box_placement(cell_cap):
    for r in ranges:

        min = int(ranges[r].split('-')[0])
        max = int(ranges[r].split('-')[1])

        if cell_cap in range(min, max):
            return r


def barcode_reader():

    #ports = glob.glob('/dev/ttyACM[0-9]*')
    #print(ports[0])
    #fp = open(ports[0], 'rb')

    for port, desc, hwid in sorted(ports):
        #print("{}: {} [{}]".format(port, desc, hwid))

        scanner = PD9530(port)
        scanner.attach()

    for code in scanner.readlines():
        c_split = code.split("-")
        c_cap_raw = c_split[-1]
        c_cap = int(c_cap_raw[1:].rstrip())
        box_place = box_placement(c_cap)
        str_to_print =  "Cell Cap: %s, Box: %s" % (c_cap, box_place)
        print(str_to_print)

    scanner.close()


if __name__ == '__main__':
    try:
        while True:
            barcode_reader()

    except KeyboardInterrupt:
        pass