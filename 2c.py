from pprint import pprint
import napalm
from my_devices import cisco3, arista1
from my_functions import connect
#from lxml import etree


print()
device_list = [cisco3, arista1]
conn_dev =[]
for device in device_list:
    conn_dev.append(connect(device))
    
for device in conn_dev:
    print(device.hostname)
    pprint(device.get_ntp_peers())
    print(device.platform)








'''
def check_connected(device):
    if device.connected:
        print(f'connected :)')
        return True
    else:
        print('cannot connect!!!')
        return False
        
def gather_routes(device):
    return RouteTable(device).get()

def gather_arp_table(device):
    return ArpTable(device).get()

def print_output(device,RT,ARP):
    print(device.facts['hostname'])
    print(f'device: \n port:{device.port}\nusername: {device.user}')
    print()    
    pprint(RT.items())
    print()
    pprint(ARP.items())

device = Device(**srx2)

print()
#with device.open() as dev:
device.open()
if check_connected(device):
    device_cfg = Config(device)
    print()
    show_xml = device.rpc.get_software_information()
    print(show_xml)
    print()
    print(etree.tostring(show_xml, encoding='unicode'))
    print()
    intf_xml = device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
    print(etree.tostring(intf_xml, encoding='unicode', pretty_print=True))

#    RT = gather_routes(device)
#    device_cfg.load(path='StaticRoutes.cfg', format='text', merge=True)
#    print(device_cfg.diff())
#    device_cfg.commit()


#    try:
#        device_cfg.lock()
#        print('locked successfully')
#        print('stage conf using set command')
#        device_cfg.load('set system host-name blablaba', format='set', merge=True)
#        print(device_cfg.diff())
#        print('rollback..')
#        device_cfg.rollback()
#        print(device_cfg.diff())
#    except LockError:
#        print('!already locked!')

#        ARP = gather_arp_table(dev)
#        print_output(dev,RT,ARP)

'''
print()
