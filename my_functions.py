#from jnpr.junos import Device
#from jnpr.junos.op.ethport import EthPortTable
#from jnpr.junos.op.arp import ArpTable
#from jnpr.junos.op.routes import RouteTable
#from pprint import pprint
import napalm
#from my_devices import cisco3, arista1
#from jnpr_devices import srx2
#from jnpr.junos.utils.config import Config
#from jnpr.junos.exception import LockError
#from lxml import etree

def connect(device):
    device = device.copy()
    driver = napalm.get_network_driver(device['driver'])
    device.pop("driver")
    device = driver(**device)
    device.open()
    return device

def create_backup(connection):

    backup=connection.get_config()
    filename = f"{connection.hostname}-running.txt"
    with open(filename, "w") as f:
         f.write(backup["running"])

def create_checkpoint(connection):
    if "nxos" in connection.platform:
        filename = f"{connection.hostname}-checkpoint.txt"
        backup=connection._get_checkpoint_file()
        with open(filename, "w") as f:
            f.write(backup)
    else:
        print(f"{connection.hostname} it is not NX-OS")
        #raise ValueError("It is not NX-OS, checkpoint requires NX-OS")
