from opcua import Client

SERVER_URL = "opc.tcp://10.1.54.231:51310/CogentDataHub/DataAccess"

client = Client(SERVER_URL)


def count_nodes(node, count=0):
    """Recursively count all child nodes of a given node."""
    count += 1
    children = node.get_children()
    for child in children:
        count = count_nodes(child, count)
    return count


try:
    client.connect()
    print("Connected to OPC UA server")

    root = client.get_root_node()
    total_nodes = count_nodes(root)

    print(f"Total number of nodes: {total_nodes}")

except Exception as e:
    print("Error:", e)

finally:
    client.disconnect()
    print("Disconnected from OPC UA server")
