
import asyncio
import csv
from datetime import datetime
from asyncua import Client, ua


async def browse_variable_nodes(client, parent_node_id):
    node = client.get_node(parent_node_id)
    all_variable_nodes = []

    try:
        references = await node.browse(descendants=False)

        for ref in references:
            if ref.NodeClass == ua.NodeClass.Variable:
                all_variable_nodes.append(ref.NodeId)

        # Optional: Browse deeper levels here if needed

        return all_variable_nodes

    except Exception as e:
        print("Browsing error:", e)
        return []


async def read_node_value(client, node_id):
    try:
        node = client.get_node(node_id)
        value = await node.read_value()
        data_type = await node.read_data_type_as_variant_type()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{node_id} -> {value} ({data_type.name}) at {timestamp}")
        return str(node_id), str(value), data_type.name, timestamp
    except Exception as e:
        print(f"Error reading {node_id}: {e}")
        return str(node_id), "Error", "Unknown", datetime.now().strftime("%Y-%m-%d %H:%M:%S")


async def main():
    server_url = "opc.tcp://10.1.54.231:51310/CogentDataHub/DataAccess"
    root_node_id = "ns=2;s=default"

    async with Client(url=server_url) as client:
        print("Connected to OPC UA server")

        print("Browsing for Variable nodes only...")
        variable_node_ids = await browse_variable_nodes(client, root_node_id)
        print(f"Found {len(variable_node_ids)} variable nodes under '{root_node_id}'")

        if not variable_node_ids:
            print("No variable nodes found. Exiting.")
            return

        # Read node values
        results = await asyncio.gather(*[read_node_value(client, nid) for nid in variable_node_ids])

        # Save to CSV
        csv_file = "realtime_opcua_data.csv"
        with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["NodeId", "Value", "DataType", "Timestamp"])
            writer.writerows(results)

        print(f"\nRealtime data saved to {csv_file}")


if __name__ == "__main__":
    asyncio.run(main())
