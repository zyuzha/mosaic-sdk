import logging
from typing import Dict, Optional
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NavigationError(Exception):
    """Custom exception for navigation-related errors"""
    pass


class ExplorationMode(Enum):
    """Enumeration of available exploration modes"""
    SAFE = auto()
    AGGRESSIVE = auto()
    STEALTH = auto()


class Navigator:
    """
    A class to manage exploration in the Infinite Backrooms simulation.
    
    Attributes:
        current_location (str): Current position in the simulation
        _visited_locations (dict): History of visited locations
        _exploration_mode (ExplorationMode): Current exploration strategy
    """
    
    def __init__(self, start_location: str = "Starting Point"):
        """
        Initialize the Navigator with a starting location.
        
        Args:
            start_location: Initial location in the simulation
            
        Raises:
            ValueError: If start_location is empty or invalid
        """
        if not start_location or not isinstance(start_location, str):
            raise ValueError("Start location must be a non-empty string")
        
        self.current_location = start_location
        self._visited_locations = {start_location: 1}
        self._exploration_mode = ExplorationMode.SAFE
        logger.info(f"Navigator initialized at {start_location}")

    def set_exploration_mode(self, mode: ExplorationMode) -> None:
        """
        Set the exploration strategy.
        
        Args:
            mode: Exploration mode from ExplorationMode enum
            
        Raises:
            ValueError: If invalid mode is provided
        """
        try:
            if not isinstance(mode, ExplorationMode):
                raise ValueError("Invalid exploration mode")
            
            self._exploration_mode = mode
            logger.info(f"Exploration mode set to {mode.name}")
        except ValueError as e:
            logger.error(f"Failed to set exploration mode: {str(e)}")
            raise

    def explore(self, direction: Optional[str] = None) -> str:
        """
        Explore new areas in the simulation.
        
        Args:
            direction: Optional direction for exploration
            
        Returns:
            str: New location identifier
            
        Raises:
            NavigationError: If exploration fails
        """
        try:
            if direction and not isinstance(direction, str):
                raise ValueError("Direction must be a string or None")
            
            new_location = self._generate_new_location(direction)
            
            # Update location tracking
            self._visited_locations[new_location] = (
                self._visited_locations.get(new_location, 0) + 1
            )
            self.current_location = new_location
            
            logger.info(f"Explored to {new_location} in {self._exploration_mode.name} mode")
            return new_location
            
        except Exception as e:
            logger.error(f"Exploration failed: {str(e)}")
            raise NavigationError(f"Exploration failed: {str(e)}") from e

    def get_current_location(self) -> str:
        """Return the current location"""
        return self.current_location

    def get_exploration_history(self) -> Dict[str, int]:
        """
        Get the complete exploration history.
        
        Returns:
            dict: Mapping of locations to visit counts
        """
        return self._visited_locations.copy()

    def _generate_new_location(self, direction: Optional[str]) -> str:
        """
        Generate a new location based on exploration parameters.
        
        Args:
            direction: Optional direction for exploration
            
        Returns:
            str: Generated location identifier
        """
        try:
            if direction:
                return f"{direction.capitalize()} Realm"
            return "New Realm"
        except Exception as e:
            logger.error(f"Failed to generate new location: {str(e)}")
            raise NavigationError("Error in generating new location")

    def __repr__(self) -> str:
        """Official string representation of the Navigator"""
        return (f"Navigator(current_location={self.current_location}, "
                f"mode={self._exploration_mode.name}, "
                f"visited={len(self._visited_locations)} locations)")
