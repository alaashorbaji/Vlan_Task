import netmiko
class connect:

    @staticmethod
    def conn(configuration=None,ip=None,device_type=None,username=None,password=None):
        conn = netmiko.ConnectHandler(ip=ip, device_type=device_type, username=username,
                                      password=password)
        output = conn.send_config_set(configuration)
        conn.disconnect()
        return output
    @staticmethod
    def show(ip=None,device_type=None,username=None,password=None):
        conn = netmiko.ConnectHandler(ip=ip, device_type=device_type, username=username,
                                      password=password)
        output = conn.send_command("show vlan",use_textfsm=True)
        conn.disconnect()
        return output
