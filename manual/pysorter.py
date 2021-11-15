import serial.tools.list_ports as port_list
import csv
from pd9530 import PD9530

ports = list(port_list.comports())
#
# for port in ports:
#     print(port)

cells = []
cells_codes = []

packs = {}

try:
    with open('Cells.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            cell_string = (', '.join(row))
            # cells_codes.append(cell_string)
            #
            # cell_split = cell_string.split("-")
            # cell_cap_raw = cell_split[-1]
            # cell_cap = cell_cap_raw[1:]
            cells.append(cell_string)

        cells = (', '.join(cells))
        with open("rpkrcells.txt", "w") as f:
            f.write(cells)
        print(cells)
except:
    print("Cells.csv not present, index and try again")


try:
    with open('packs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        try:
            for row in spamreader:
                cell_id = row[0].split(',')[0]
                cell_cap = row[0].split(',')[1]


                if cell_id not in packs:
                    packs[cell_id] = []
                packs[cell_id].append(cell_cap)

            print(packs)
        except:
            print("packs.csv not formatted properly")
except:
    print("packs.csv does not exist, generate and try again")

def check_cell(code):

    found = False

    for cell in packs:
        # print(packs[cell])

        c_split = code.split("-")
        c_cap_raw = c_split[-1]
        c_cap = c_cap_raw[1:].rstrip()
        if c_cap in packs[cell]:
            print("Cell ID: %s" % cell)
            packs[cell].remove(c_cap)
            print(packs[cell])
            found = True
            break

    if not found:
        print ("Cell not found: %s" % code)


def check_single_cell(code):

    found = False
    cell = "4"
    # print(packs[cell])

    c_split = code.split("-")
    c_cap_raw = c_split[-1]
    c_cap = c_cap_raw[1:].rstrip()
    if c_cap in packs[cell]:
        print("Cell ID: %s" % cell)
        packs[cell].remove(c_cap)
        print(packs[cell])
        found = True

    if not found:
        print ("Cell not found: %s" % code)


def barcode_reader():

    #ports = glob.glob('/dev/ttyACM[0-9]*')
    #print(ports[0])
    #fp = open(ports[0], 'rb')

    for port, desc, hwid in sorted(ports):
        #print("{}: {} [{}]".format(port, desc, hwid))

        scanner = PD9530(port)
        scanner.attach()

    for code in scanner.readlines():
        check_cell(code)
        print(code)

    scanner.close()


if __name__ == '__main__':
    try:
        while True:
            barcode_reader()

    except KeyboardInterrupt:
        pass