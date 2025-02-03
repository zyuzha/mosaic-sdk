import time
import random
from mosaic.connection import Connector, ConnectionError

def simulate_operation(connector, operation_number: int) -> None:
    """
    Simulate a single operation in the simulation environment.

    This function performs a dummy operation and randomly decides whether
    to send a heartbeat during the operation to verify connection stability.

    Args:
        connector (Connector): The active connector instance.
        operation_number (int): The current operation number for logging.
    """
    print(f"Operation {operation_number}: Starting...")
    # Simulate operation delay
    time.sleep(random.uniform(0.5, 1.5))
    
    # Randomly decide whether to perform a heartbeat check during this operation
    if random.choice([True, False]):
        try:
            if connector.send_heartbeat():
                print(f"Operation {operation_number}: Heartbeat check passed.")
        except ConnectionError as e:
            print(f"Operation {operation_number}: Heartbeat check failed with error: {e}")
            # Depending on the application's need, you could choose to raise the error
            # or continue with the operation. Here, we choose to raise it.
            raise
    else:
        print(f"Operation {operation_number}: No heartbeat check performed.")
    
    # Simulate additional operation logic
    print(f"Operation {operation_number}: Completed.\n")

try:
    # Establish connection using a context manager
    with Connector(agent="AI-Explorer-Complex") as connector:
        print(f"Agent '{connector.agent}' connection established: {connector.is_connected}\n")
        
        # Simulate multiple operations in the simulation environment
        for i in range(1, 6):
            try:
                simulate_operation(connector, i)
            except ConnectionError as op_error:
                print(f"Operation {i}: Terminating due to connection error: {op_error}")
                break
        
        # After all operations, perform a final heartbeat check
        try:
            if connector.send_heartbeat():
                print("Final heartbeat check passed. Connection is stable.")
        except ConnectionError as final_error:
            print(f"Final heartbeat check failed with error: {final_error}")
        
except ConnectionError as e:
    print(f"Connection error encountered: {e}")
