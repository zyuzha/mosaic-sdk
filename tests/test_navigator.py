import unittest
from navigator_with_items import Navigator, ExplorationMode, ItemType, Item, NavigationError

class TestNavigator(unittest.TestCase):
    def setUp(self):
        """Setup a fresh Navigator instance before each test."""
        self.navigator = Navigator()
    
    def test_initial_state(self):
        """Test if the Navigator initializes correctly."""
        self.assertEqual(self.navigator.get_current_location(), "Starting Point")
        self.assertEqual(self.navigator.get_energy(), Navigator.MAX_ENERGY)
        self.assertEqual(len(self.navigator.get_inventory()), 0)
    
    def test_exploration_mode_change(self):
        """Test setting different exploration modes."""
        self.navigator.set_exploration_mode(ExplorationMode.AGGRESSIVE)
        self.assertEqual(self.navigator._exploration_mode, ExplorationMode.AGGRESSIVE)
        
        self.navigator.set_exploration_mode(ExplorationMode.STEALTH)
        self.assertEqual(self.navigator._exploration_mode, ExplorationMode.STEALTH)
    
    def test_exploration_energy_consumption(self):
        """Test if energy decreases correctly after exploring."""
        initial_energy = self.navigator.get_energy()
        self.navigator.explore("North")
        self.assertEqual(self.navigator.get_energy(), initial_energy - Navigator.ENERGY_COST)
    
    def test_exploration_without_energy(self):
        """Test if an error is raised when trying to explore without energy."""
        self.navigator._energy = 0
        with self.assertRaises(NavigationError):
            self.navigator.explore("East")
    
    def test_restores_energy(self):
        """Test if resting restores energy correctly."""
        self.navigator._energy = 50
        self.navigator.rest()
        self.assertEqual(self.navigator.get_energy(), 80)  # 50 + 30 restore
        
        self.navigator.rest()
        self.assertEqual(self.navigator.get_energy(), 100)  # Max energy limit
    
    def test_item_collection_during_exploration(self):
        """Test if items can be collected during exploration."""
        initial_inventory_size = len(self.navigator.get_inventory())
        
        # Simulate multiple explorations to ensure an item is found
        for _ in range(10):
            self.navigator.explore("West")
        
        self.assertGreater(len(self.navigator.get_inventory()), initial_inventory_size)
    
    def test_use_item(self):
        """Test using an item from inventory."""
        item = Item("Energy Bar", ItemType.FOOD, "Restores 20 energy")
        self.navigator._inventory.append(item)
        
        self.assertIn(item, self.navigator.get_inventory())
        self.navigator.use_item("Energy Bar")
        self.assertNotIn(item, self.navigator.get_inventory())
    
    def test_use_non_existent_item(self):
        """Test attempting to use an item that is not in inventory."""
        initial_inventory_size = len(self.navigator.get_inventory())
        self.navigator.use_item("Non-Existent Item")
        self.assertEqual(len(self.navigator.get_inventory()), initial_inventory_size)
    
if __name__ == "__main__":
    unittest.main()
