from opcua import Client
import comma_seperated_values
import os


def export_simulation_tags_to_csv():
    folder_path = "C:\\nodes"
    csv_filename = os.path.join(folder_path, "simulation_tags.comma_seperated_values")

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # OPC UA server URL
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

        # Writing data to CSV File
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = comma_seperated_values.writer(csv_file)
            writer.writerow(["Browse Name", "Node ID", "Value"])

            print("Tags under 'Simulation':")
            for child in children:
                browse_name = child.get_browse_name().Name
                node_id = str(child.nodeid)
                try:
                    value = child.get_value()
                except:
                    value = "<Non-readable>"
                print(f"Name: {browse_name}, NodeId: {node_id}, Value: {value}")
                writer.writerow([browse_name, node_id, value])

        # Count total number of nodes
        print(f"Total nodes under 'Simulation': {len(children)}")
        print(f"Data exported to: {csv_filename}")

    finally:
        client.disconnect()
        print("Disconnected from server")


# Run the function
if __name__ == "__main__":
    export_simulation_tags_to_csv()
