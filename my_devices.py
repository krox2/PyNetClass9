from getpass import getpass
pwd = getpass()
cisco3 = { 'hostname': 'cisco3.lasthop.io', 'username': 'pyclass', 'password': pwd, 'driver': 'ios'}
arista1 = { 'hostname': 'arista1.lasthop.io', 'username': 'pyclass','password': pwd, 'driver': 'eos'}
nxos1 = { 'hostname': 'nxos1.lasthop.io', 'username': 'pyclass','password': pwd, 'driver': 'nxos', 'optional_args': {'port': 8443} }
