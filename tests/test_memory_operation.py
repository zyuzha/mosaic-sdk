import unittest
from mosaic.learning.memory_store import MemoryStore, MemoryError
from mosaic.learning.memory_operation import MemoryOperations

class TestMemoryOperations(unittest.TestCase):
    def setUp(self):
        self.memory_store = MemoryStore()
        self.memory_operations = MemoryOperations(self.memory_store)
        self.memory_store._memory = {"key": "value"}  # Pre-populate memory for testing

    def test_clear_memory(self):
        with self.assertLogs('mosaic.learning.memory_operations', level='INFO') as log:
            self.memory_operations.clear_memory()
            self.assertEqual(self.memory_store._memory, {})
            self.assertIn("INFO:mosaic.learning.memory_operations:Memory store cleared successfully.", log.output)

    def test_clear_memory_failure(self):
        with self.assertLogs('mosaic.learning.memory_operations', level='ERROR') as log:
            with unittest.mock.patch.object(self.memory_store, 'clear', side_effect=Exception("Clear failed")):
                with self.assertRaises(MemoryError):
                    self.memory_operations.clear_memory()
                self.assertIn("ERROR:mosaic.learning.memory_operations:Failed to clear memory store: Clear failed", log.output)

if __name__ == '__main__':
    unittest.main()