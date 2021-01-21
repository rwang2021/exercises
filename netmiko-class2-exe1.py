from netmiko import ConnectHandler
from getpass import getpass

def cisco4():
    global net_connect
    cisco = {'device_type':'cisco_xe',
           'host':'cisco4.lasthop.io',
           'username':'pyclass',
           'password':getpass,
           'port':22,}
    net_connect = ConnectHandler(**cisco)

    print(net_connect.find_prompt())

    ping = net_connect.send_command('ping\n', expect_string=':')
    ping += net_connect.send_command('\n', expect_string=':')
    ping += net_connect.send_command('8.8.8.8\n', expect_string=':')
    ping += net_connect.send_command('\n', expect_string=':')
    ping += net_connect.send_command('\n', expect_string=':')
    ping += net_connect.send_command('\n', expect_string=':')
    ping += net_connect.send_command('\n', expect_string=':')
    ping += net_connect.send_command('\n', expect_string=':')
    print(ping)

    pingt = net_connect.send_command_timing('ping\n', strip_command=False, strip_prompt=False)
    pingt += net_connect.send_command_timing('\n', strip_command=False, strip_prompt=False)
    pingt += net_connect.send_command_timing('8.8.8.8\n', strip_command=False, strip_prompt=False)
    pingt += net_connect.send_command_timing('\n', strip_command=False, strip_prompt=False)
    pingt += net_connect.send_command_timing('\n', strip_command=False, strip_prompt=False)
    pingt += net_connect.send_command_timing('\n', strip_command=False, strip_prompt=False)
    pingt += net_connect.send_command_timing('\n', strip_command=False, strip_prompt=False)
    pingt += net_connect.send_command_timing('\n', strip_command=False, strip_prompt=False)
    print(ping)

    net_connect.disconnect()

#Main function
def main():
    cisco4()

if __name__ == '__main__':
    main()
#END of script