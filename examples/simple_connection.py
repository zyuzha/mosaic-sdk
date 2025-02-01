from mosaic.connection import Connector, ConnectionError

try:
    with Connector(agent="AI-Explorer-001") as connector:
        print(f"Connected: {connector.is_connected}")
        # Perform operations in the simulation
except ConnectionError as e:
    print(f"Connection failed: {e}")