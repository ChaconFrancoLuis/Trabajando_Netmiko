#ejemplo con tutorial de github
from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.6',
    'username': 'cisco',
    'password': 'cisco123!',
    'port' : 22}


#net_connect = ConnectHandler(**cisco_881)

config_commands = ["interface vlan 2",
                   "ip address 192.168.0.6 255.255.255.0",
                   "no shut"]

net_connect = ConnectHandler(**cisco_881)

output = net_connect.send_config_set(config_commands)
print(output)

