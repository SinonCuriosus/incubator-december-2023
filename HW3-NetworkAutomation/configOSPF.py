from ncclient import manager
import xml.dom.minidom

def get_ospf_config(host, username, password):
    """
    Retrieve OSPF configuration from a Cisco router using NETCONF.
    """

    # Define NETCONF filter to get OSPF configuration
    ospf_filter = '''
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <router>
                    <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf"/>
                </router>
            </native>
        </filter>
    '''

    # Establish NETCONF connection to the device
    with manager.connect(host=host, port=830, username=username, password=password,
                         hostkey_verify=False, device_params={'name': 'csr'}) as m:

        # Retrieve OSPF configuration
        ospf_config = m.get_config(source='running', filter=ospf_filter)

        # Print OSPF configuration
        print(xml.dom.minidom.parseString(ospf_config.xml).toprettyxml())

def configure_ospf(host, username, password, ospf_config):
    """
    Configure OSPF on a Cisco router using NETCONF.
    """

    # Establish NETCONF connection to the device
    with manager.connect(host=host, port=830, username=username, password=password,
                         hostkey_verify=False, device_params={'name': 'csr'}) as m:

        # Send OSPF configuration
        m.edit_config(target='running', config=ospf_config)

        print("OSPF configuration applied successfully.")

if __name__ == '__main__':
    # Specify the device details
    host = '10.10.20.48'
    username = 'developer'
    password = 'C1sco12345'

    # Call the function to retrieve OSPF configuration
    get_ospf_config(host, username, password)

    # Example OSPF configuration payload
    ospf_config = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <router>
                    <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                        <id>1</id>
                        <!-- Add your OSPF configuration here -->
                    </ospf>
                </router>
            </native>
        </config>
    '''

    # Call the function to configure OSPF
    configure_ospf(host, username, password, ospf_config)
