from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException

router = {
    "host":"192.168.0.7",
    "port":22,
    "username":"cisco",
    "password":"cisco123!1",
    "device_type":"cisco_ios"
}

configurar = ["no interface loopback 11"]

try:
    A = ConnectHandler(**router)
    A.enable()
    A.send_config_set(configurar)
    respuesta = A.send_command("show ip int brief")
    save = A.save_config()
    print("saving running config......")
    A.disconnect()
    print("user has exited tty session...")
except Exception as ex:
    print(ex)
else:
    print(respuesta)
