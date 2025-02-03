import logging
from typing import Optional

# Configure logging with timestamp and format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class ConnectionError(Exception):
    """Custom exception for connection-related errors"""
    pass


class Connector:
    """
    A class to manage connections to the Infinite Backrooms simulation environment.
    
    Attributes:
        agent (str): Identifier for the AI agent
        _connected (bool): Connection status flag
    """
    
    def __init__(self, agent: str):
        """
        Initialize the Connector with a specific AI agent.
        
        Args:
            agent: Unique identifier for the AI agent
            
        Raises:
            ValueError: If agent is empty or not a string
        """
        if not agent or not isinstance(agent, str):
            raise ValueError("Agent must be a non-empty string")
            
        self.agent = agent
        self._connected = False

    @property
    def is_connected(self) -> bool:
        """Return the current connection status"""
        return self._connected

    def connect(self, timeout: int = 10) -> None:
        """
        Establish connection to the simulation environment.
        
        Args:
            timeout: Connection timeout in seconds
            
        Raises:
            ConnectionError: If connection cannot be established
        """
        try:
            if self._connected:
                logger.warning(f"{self.agent}: Already connected")
                return

            # Simulated connection logic
            logger.debug(f"{self.agent}: Attempting connection...")
            
            # Replace with actual connection logic
            if timeout < 1:
                raise ConnectionError("Invalid timeout value")
                
            self._connected = True
            logger.info(f"{self.agent}: Successfully connected to Infinite Backrooms")

        except Exception as e:
            self._connected = False
            logger.error(f"{self.agent}: Connection failed - {str(e)}")
            raise ConnectionError(f"Connection failed: {str(e)}") from e

    def disconnect(self) -> None:
        """
        Terminate the current connection gracefully.
        
        Raises:
            ConnectionError: If disconnection fails
        """
        try:
            if not self._connected:
                logger.warning(f"{self.agent}: Not currently connected")
                return

            # Simulated disconnection logic
            logger.debug(f"{self.agent}: Initiating disconnect...")
            
            # Replace with actual disconnection logic
            self._connected = False
            logger.info(f"{self.agent}: Disconnected from Infinite Backrooms")

        except Exception as e:
            logger.error(f"{self.agent}: Disconnection failed - {str(e)}")
            raise ConnectionError(f"Disconnection failed: {str(e)}") from e

    def __enter__(self):
        """Context manager entry point"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point"""
        self.disconnect()

    def __repr__(self) -> str:
        """Official string representation of the Connector"""
        return f"Connector(agent={self.agent}, connected={self._connected})"

    def send_heartbeat(self) -> bool:
        """
        Send a heartbeat signal to verify the connection status.
        
        Returns:
            bool: True if the connection is active and the heartbeat is successful.
        
        Raises:
            ConnectionError: If the heartbeat cannot be sent because the connection is not active.
        
        Examples:
            >>> connector = Connector("Agent007")
            >>> connector.connect()
            >>> connector.send_heartbeat()
            True
        """
        if not self._connected:
            logger.error(f"{self.agent}: Cannot send heartbeat. Not connected.")
            raise ConnectionError("Cannot send heartbeat. Not connected.")

        try:
            # Simulate heartbeat logic. In a real scenario, replace this with actual ping logic.
            logger.debug(f"{self.agent}: Sending heartbeat...")
            
            # Assuming heartbeat is always successful in this simulation.
            logger.info(f"{self.agent}: Heartbeat successful")
            return True
        except Exception as e:
            logger.error(f"{self.agent}: Heartbeat failed - {str(e)}")
            raise ConnectionError(f"Heartbeat failed: {str(e)}") from e
