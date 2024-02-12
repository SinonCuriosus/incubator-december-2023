from ncclient import manager
import xml.dom.minidom

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
</filter>"""

# Define the VLAN configuration
vlan_config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>VLAN10</name>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">softwareLoopback</type>
            <enabled>true</enabled>
            <description>My VLAN 10</description>
        </interface>
    </interfaces>
</config>
"""

# Establish NETCONF connection and create VLAN
with manager.connect(
        host='10.10.20.48',
        port='830',
        username='developer',
        password='C1sco12345',
        hostkey_verify=False,
        device_params={'name': "csr"}
        ) as m:

    # Retrieve existing configuration using get-config
    try:
        print("Retrieving existing configuration...")
        result = m.get_config(source='running', filter=netconf_filter)
        print("Existing configuration retrieved successfully.")
        
        # Print the retrieved configuration for examination
        print("Retrieved configuration:")
        print(xml.dom.minidom.parseString(result.xml).toprettyxml())
        
    except Exception as e:
        print("Failed to retrieve existing configuration:", e)
