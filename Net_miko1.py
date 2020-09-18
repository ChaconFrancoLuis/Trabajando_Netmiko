from netmiko import ConnectHandler


sshCli = {
    'device_type'="cisco_ios",
    'host'="192.168.0.6",
    'port'=22,
    'username'="cisco",
    'password'="cisco123!"
    }

net_connect = ConnectHandler(**sshCli)
output = sshCli.send_command("show ip interface brief")
print(output)



