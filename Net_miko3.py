from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

router = {
    "host":"192.168.0.6",
    "port":22,
    "username":"cisco",
    "password":"cisco123!",
    "device_type":"cisco_ios"
}

configurar = ["no interface loopback 11"]

#try:
    A = ConnectHandler(**router)
    on = A.enable()
    A.send_config_set(configurar)
    respuesta = A.send_command("show ip int brief")
    #save = A.save_config()
    #print("saving running config......")
   # off = A.disconnect()
  #  print("user has exited tty session...")

#except NetMikoTimeoutException:
 #       print ('Device not reachable' )

#except NetMikoAuthenticationException:
        print ('Authentication Failure' )

#except SSHException:
        print ('Make sure SSH is enabled' )
        
#else:
#    print(respuesta)
