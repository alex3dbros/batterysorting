import paramiko
from scp import SCPClient
from shutil import copyfile
import time

raspberry = "192.168.1.244"

def deploy(client_ip, username, password):

    paramiko.util.log_to_file("ssh.log")
    ssh = paramiko.SSHClient()

    # SCPCLient takes a paramiko transport as an argument

    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(client_ip, username=username, password=password, timeout=30)
    scp = SCPClient(ssh.get_transport())

    print ("copy to Sorter")
    scp.put("run.py", '/home/pi/batterysorting/')
    scp.put("testing.py", '/home/pi/batterysorting/')
    scp.put("switch.py", '/home/pi/batterysorting/')
    scp.put("functions.py", '/home/pi/batterysorting/')
    scp.put("nema.py", '/home/pi/batterysorting/')
    scp.put("motorThread.py", '/home/pi/batterysorting/')
    scp.put("webcam.py", '/home/pi/batterysorting/')
    scp.put("webcam_test.py", '/home/pi/batterysorting/')

    scp.close()
    ssh.close()


deploy(raspberry, "pi", "raspberry")