import logging
from typing import Dict, Optional
from enum import Enum, auto
import random


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NavigationError(Exception):
    """Custom exception for navigation-related errors."""
    pass


class ExplorationMode(Enum):
    """Enumeration of available exploration modes."""
    SAFE = auto()
    AGGRESSIVE = auto()
    STEALTH = auto()


class Navigator:
    """
    A class to manage exploration in the Infinite Backrooms simulation.
    
    Attributes:
        MAX_ENERGY (int): Maximum energy level.
        ENERGY_COST (int): Energy consumed per exploration.
        RESTORE_ENERGY (int): Energy restored when resting.
        current_location (str): The current location of the navigator.
        _visited_locations (dict): A dictionary storing visited locations and their visit count.
        _exploration_mode (ExplorationMode): The current exploration strategy.
        _energy (int): The remaining energy level.
        _exploration_map (dict): A dictionary tracking exploration paths.
    """
    MAX_ENERGY = 100
    ENERGY_COST = 10
    RESTORE_ENERGY = 30
    
    def __init__(self, start_location: str = "Starting Point"):
        """
        Initialize the Navigator with a starting location.
        
        Args:
            start_location (str): The initial location in the simulation.
        
        Raises:
            ValueError: If start_location is not a valid string.
        """
        try:
            if not start_location or not isinstance(start_location, str):
                raise ValueError("Start location must be a non-empty string")
            
            self.current_location = start_location
            self._visited_locations = {start_location: 1}
            self._exploration_mode = ExplorationMode.SAFE
            self._energy = self.MAX_ENERGY
            self._exploration_map = {start_location: []}
            
            logger.info(f"Navigator initialized at {start_location}")
        except ValueError as e:
            logger.error(f"Initialization failed: {str(e)}")
            raise
    
    def set_exploration_mode(self, mode: ExplorationMode) -> None:
        """
        Set the exploration strategy.
        
        Args:
            mode (ExplorationMode): The exploration mode from the ExplorationMode enum.
        
        Raises:
            ValueError: If an invalid mode is provided.
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
            direction (str, optional): The direction for exploration.
        
        Returns:
            str: The identifier of the new location.
        
        Raises:
            NavigationError: If exploration fails due to lack of energy.
            ValueError: If direction is not a valid string.
        """
        try:
            if self._energy < self.ENERGY_COST:
                raise NavigationError("Not enough energy to explore. Please rest.")
            
            if direction and not isinstance(direction, str):
                raise ValueError("Direction must be a string or None")
            
            new_location = self._generate_new_location(direction)
            
            self._visited_locations[new_location] = (
                self._visited_locations.get(new_location, 0) + 1
            )
            self.current_location = new_location
            self._energy -= self.ENERGY_COST
            
            # Update exploration map
            if new_location not in self._exploration_map:
                self._exploration_map[new_location] = []
            self._exploration_map[self.current_location].append(new_location)
            
            logger.info(f"Explored to {new_location} in {self._exploration_mode.name} mode")
            return new_location
        except (NavigationError, ValueError) as e:
            logger.error(f"Exploration failed: {str(e)}")
            raise
    
    def rest(self):
        """
        Restore energy after resting.
        """
        try:
            self._energy = min(self._energy + self.RESTORE_ENERGY, self.MAX_ENERGY)
            logger.info(f"Rested and restored energy to {self._energy}")
        except Exception as e:
            logger.error(f"Failed to restore energy: {str(e)}")
            raise
    
    def get_current_location(self) -> str:
        """Return the current location."""
        return self.current_location
    
    def get_exploration_history(self) -> Dict[str, int]:
        """
        Get the complete exploration history.
        
        Returns:
            dict: A dictionary mapping locations to visit counts.
        """
        return self._visited_locations.copy()
    
    def get_exploration_map(self) -> Dict[str, list]:
        """
        Get the exploration map.
        
        Returns:
            dict: A dictionary mapping locations to the list of connected locations.
        """
        return self._exploration_map.copy()
    
    def _generate_new_location(self, direction: Optional[str]) -> str:
        """
        Generate a new location based on exploration parameters.
        
        Args:
            direction (str, optional): The direction for exploration.
        
        Returns:
            str: The generated location identifier.
        """
        try:
            if direction:
                return f"{direction.capitalize()} Realm"
            return "New Realm"
        except Exception as e:
            logger.error(f"Failed to generate new location: {str(e)}")
            raise NavigationError("Error in generating new location")
    
    def get_energy(self) -> int:
        """Returns the current energy level."""
        return self._energy
    
    def __repr__(self) -> str:
        """Official string representation of the Navigator."""
        return (f"Navigator(current_location={self.current_location}, "
                f"mode={self._exploration_mode.name}, "
                f"energy={self._energy}, "
                f"visited={len(self._visited_locations)} locations)")
    
    def discard_item(self, item_name: str):
        """
        Remove an item from the inventory.

        Args:
            item_name (str): The name of the item to discard.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for item in self._inventory:
            if item.name.lower() == item_name.lower():
                self._inventory.remove(item)
                logger.info(f"Discarded item: {item.name}")
                return
        logger.warning(f"Item '{item_name}' not found in inventory.")
        raise ValueError("Item not found in inventory.")
    
    def find_random_item(self):
        """
        Attempt to find a random item while exploring.

        There is a 40% chance of finding an item.

        Returns:
            Optional[Item]: The found item, or None if no item is found.
        """
        if random.random() < 0.4:  # 40% chance to find an item
            found_item = random.choice(self.POSSIBLE_ITEMS)
            self._inventory.append(found_item)
            logger.info(f"Found an item: {found_item.name}")
            return found_item
        logger.info("No item found this time.")
        return None

