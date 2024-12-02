from netmiko import ConnectHandler


router = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22,
}

with ConnectHandler(**router) as net_connect:
    
    print("Afficher l'heure :")
    output_clock = net_connect.send_command("show clock")
    print(output_clock)

   
    print("\nRécupérer des interfaces...")
    output_interfaces = net_connect.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as file:
        file.write(output_interfaces)

    
    print("\nConfigurer l'interface loopback...")
    config_commands = [
        "interface loopback0",
        "ip address 10.8.8.8 255.255.255.240",
    ]
    net_connect.send_config_set(config_commands)
    print("Configuration terminée.")

    
    output_verify = net_connect.send_command("show ip interface brief | include Loopback")
    print("\nVérification :")
    print(output_verify)
