from ncclient import manager
from ncclient.operations import RPCError
import xmltodict


def show_interface_brief(interfaces):
    for interface in interfaces:
        print(f"Interface Name: {interface['name']}")
    if 'description' in interface:
        print(f"Description: {interface['description']}")
    print(f"Enabled: {interface['enabled']}")
    if 'ipv4' in interface:
        if 'address' in interface['ipv4']:
            print(f"IPv4 Address: {interface['ipv4']['address']['ip']}")
            print(f"IPv4 Netmask: {interface['ipv4']['address']['netmask']}")
        else:
            print("IPv4 Address: Not configured")
    else:
        print("IPv4 Address: Not configured")
    if 'ipv6' in interface:
        if 'address' in interface['ipv6']:
            print(f"IPv6 Address: {interface['ipv6']['address']['ip']}")
        else:
            print("IPv6 Address: Not configured")
    else:
        print("IPv6 Address: Not configured")
    print("=================================================================")

# NETCONF payload to add a loopback interface
payload = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>111</name>
                <description>My first loopback through NETCONF</description>
                <ip>
                    <address>
                        <primary>
                            <address>1.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
'''

# Function to add loopback interface
def add_loopback_interface(connection, config):
    try:
        response = connection.edit_config(config,target = "running")
        print("Loopback interface added successfully.")
    except RPCError as e:
        print(f"Failed to add loopback interface: {e}")

# Function to retrieve interfaces
def get_interfaces(m):
    # Create an XML filter for targeted NETCONF queries
    netconf_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface></interface>
        </interfaces>
    </filter>"""

    # Retrieve configuration from running datastore
    netconf_reply = m.get_config(source='running', filter=netconf_filter)

    # Parse the returned XML to an Ordered Dictionary
    netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

    # Check if interfaces are present in the response
    if "interfaces" in netconf_data and "interface" in netconf_data["interfaces"]:
        # Retrieve interface data
        interfaces = netconf_data["interfaces"]["interface"]
        return interfaces
    else:
        print("No interfaces found.")
        return []

# Connection details
host = '10.10.20.48'
port = '830'
username = 'developer'
password = 'C1sco12345'

# Connect to device and execute operations
with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': "csr"}
) as connection:

    add_loopback_interface(connection,payload)
    print("\n\nShowing interface brief:\n")
    show_interface_brief(get_interfaces(connection))
