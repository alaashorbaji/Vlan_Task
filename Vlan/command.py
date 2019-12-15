from .connection import connect
class config():
    @staticmethod
    def comm(Vlan_id=None,Name=None,Description=None):
        Vlan_id="vlan "+Vlan_id
        Name="name "+Name
        status="no shutdown"
        if Description=="passive":
            status="shutdown"
        configuration =[Vlan_id,Name,status]
        output=connect.conn(configuration,"209.73.216.62","cisco_ios","gorjthatsmyrj","My3l@de.com")
        return output

    @staticmethod
    def delete(Vlan_id=None):
        con="no vlan "+Vlan_id
        configuration=[con]
        output = connect.conn(configuration, "209.73.216.62", "cisco_ios", "gorjthatsmyrj", "My3l@de.com")
        return output
    @staticmethod
    def update(Vlan_id=None,Name=None):
        Vlan_id="vlan "+Vlan_id
        Name="name "+Name
        configuration=[Vlan_id,Name]
        output = connect.conn(configuration, "209.73.216.62", "cisco_ios", "gorjthatsmyrj", "My3l@de.com")
        return output

    @staticmethod
    def show():
        output = connect.show( "209.73.216.62", "cisco_ios", "gorjthatsmyrj", "My3l@de.com")
        return output
