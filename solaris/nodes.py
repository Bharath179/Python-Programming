import datetime
import os

import pandas as pd
from opcua import Client

# OPC UA server settings
OPCUA_SERVER_URL = "opc.tcp://10.1.54.231:51310/CogentDataHub/DataAccess"
PARENT_NODE_ID = "ns=2;s=Default"
MAX_DATA_SIZE_BYTES = 1024
CSV_FILE = "opcua_browsed_data.csv"


def read_all_children(parent_node_id):
    client = Client(OPCUA_SERVER_URL)
    collected_data = []

    try:
        client.connect()
        print("Connected to OPC UA server.")

        parent_node = client.get_node(parent_node_id)
        children = parent_node.get_children()

        print(f"Found {len(children)} child nodes under {parent_node_id}")

        for child in children:
            try:
                child_id = child.nodeid.to_string()
                value = child.get_value()
                timestamp = datetime.datetime.now()

                encoded_value = str(value).encode('utf-8')
                if len(encoded_value) > MAX_DATA_SIZE_BYTES:
                    print(f"Skipping {child_id} — value too large")
                    continue

                collected_data.append({
                    "timestamp": timestamp,
                    "node_id": child_id,
                    "value": value
                })

            except Exception as e:
                print(f"Could not read from node {child}: {e}")

    finally:
        client.disconnect()
        print("Disconnected from OPC UA server.")

    return collected_data


def save_to_csv(data, path):
    df = pd.DataFrame(data)
    file_exists = os.path.isfile(path)

    if file_exists:
        df.to_csv(path, mode='a', header=False, index=False)
    else:
        df.to_csv(path, index=False)

    print(f"Data saved to {path}")


if __name__ == "__main__":
    data = read_all_children(PARENT_NODE_ID)

    if data:
        save_to_csv(data, CSV_FILE)
    else:
        print("No data was read.")
