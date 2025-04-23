from opcua import Client

# URL of your OPC UA server
url = "opc.tcp://DESKTOP-AJLC7JG.mshome.net:53530/OPCUA/SimulationServer"

# Connect to server
client = Client(url)
try:
    client.connect()
    print("Connected to OPC UA Server")

    # Navigate to the Simulation folder
    root = client.get_root_node()
    objects = root.get_child(["0:Objects"])
    simulation = objects.get_child(["3:Simulation"])

    # Get children of Simulation folder
    children = simulation.get_children()
    print("Tags under 'Simulation':")
    for child in children:
        browse_name = child.get_browse_name().Name
        node_id = child.nodeid
        value = None
        try:
            value = child.get_value()
        except:
            value = "<Non-readable>"
        print(f"Name: {browse_name}, NodeId: {node_id}, Value: {value}")

finally:
    client.disconnect()
    print("Disconnected from server")
