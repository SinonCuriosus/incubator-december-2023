import requests

class RESTCONFInterfaceChecker:
    def __init__(self, device_ip, username, password):
        self.device_ip = device_ip
        self.username = username
        self.password = password
        self.base_url = f"https://{self.device_ip}/restconf/data/Cisco-IOS-XE-native:native/interface/"
        self.headers = {
            'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'
        }

    def get_interfaces(self):
        url = self.base_url
        response = requests.get(url, auth=(self.username, self.password), headers=self.headers, verify=False)

        if response.status_code == 200:
            interfaces_data = response.json().get("Cisco-IOS-XE-native:interface", {})
            interfaces_info = []
            for interface_type, interfaces in interfaces_data.items():
                for interface in interfaces:
                    interface_info = {
                        'name': interface['name'],
                        'description': interface.get('description', 'Not specified'),
                        'enabled': interface.get('shutdown', 'Not specified')
                    }
                    if 'ip' in interface:
                        ip_address = interface['ip']['address']['primary']['address']
                        netmask = interface['ip']['address']['primary']['mask']
                        interface_info['ipv4_address'] = ip_address
                        interface_info['ipv4_netmask'] = netmask
                    else:
                        interface_info['ipv4_address'] = 'Not configured'
                        interface_info['ipv4_netmask'] = 'Not configured'

                    if 'ipv6' in interface:
                        ipv6_address = interface['ipv6']['address']['primary']['address']
                        interface_info['ipv6_address'] = ipv6_address
                    else:
                        interface_info['ipv6_address'] = 'Not configured'

                    interfaces_info.append(interface_info)

            return interfaces_info
        else:
            print(f"Failed to retrieve interface information. Status code: {response.status_code}")
            return []

# Example usage:
if __name__ == "__main__":
    checker = RESTCONFInterfaceChecker(device_ip='10.10.20.48', username='developer', password='C1sco12345')
    interfaces = checker.get_interfaces()
    for interface in interfaces:
        print(f"Interface Name: {interface['name']}")
        print(f"Description: {interface['description']}")
        print(f"Enabled: {interface['enabled']}")
        print(f"IPv4 Address: {interface['ipv4_address']}")
        print(f"IPv4 Netmask: {interface['ipv4_netmask']}")
        print(f"IPv6 Address: {interface['ipv6_address']}")
        print()  # Add a newline for better readability
