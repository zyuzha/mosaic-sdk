import logging

logger = logging.getLogger(__name__)

class MemoryOperations:
    def __init__(self, memory_store):
        """
        Initialize the MemoryOperations with a reference to the memory store.
        
        Args:
            memory_store: The memory store instance to operate on.
        """
        self.memory_store = memory_store

    def clear_memory(self) -> None:
        """
        Clear the entire memory store.
        
        Raises:
            MemoryError: If clearing the memory store fails.
        """
        try:
            self.memory_store.clear()
            logger.info("Memory store cleared successfully.")
        except Exception as e:
            logger.error(f"Failed to clear memory store: {str(e)}")
            raise MemoryError(f"Clearing memory store failed: {str(e)}") from e