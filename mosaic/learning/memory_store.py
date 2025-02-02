import logging
from typing import Any, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MemoryError(Exception):
    """Custom exception for memory-related errors"""
    pass


class MemoryStore:
    """
    A class to manage storage and retrieval of discoveries in the simulation.
    
    Attributes:
        _memory (List[dict]): List of stored discoveries with metadata
        _max_size (int): Maximum number of discoveries to store
    """
    
    def __init__(self, max_size: int = 1000):
        """
        Initialize the MemoryStore with a maximum capacity.
        
        Args:
            max_size: Maximum number of discoveries to store
            
        Raises:
            ValueError: If max_size is not a positive integer
        """
        if not isinstance(max_size, int) or max_size <= 0:
            raise ValueError("max_size must be a positive integer")
            
        self._memory = []
        self._max_size = max_size
        logger.info(f"MemoryStore initialized with capacity {max_size}")

    def store_discovery(self, discovery: Any, metadata: Optional[dict] = None) -> None:
        """
        Store a new discovery with optional metadata.
        
        Args:
            discovery: The discovery to store (any type)
            metadata: Optional metadata about the discovery
            
        Raises:
            MemoryError: If storage fails or capacity is reached
        """
        try:
            if len(self._memory) >= self._max_size:
                self._handle_capacity_limit()
                
            entry = {
                'timestamp': datetime.now().isoformat(),
                'discovery': discovery,
                'metadata': metadata or {}
            }
            
            self._memory.append(entry)
            logger.info(f"Stored discovery: {self._truncate_repr(discovery)}")
            
        except Exception as e:
            logger.error(f"Failed to store discovery: {str(e)}")
            raise MemoryError(f"Storage failed: {str(e)}") from e

    def retrieve_memory(self, filter_func: Optional[callable] = None) -> List[dict]:
        """
        Retrieve stored discoveries, optionally filtered.
        
        Args:
            filter_func: Optional function to filter discoveries
            
        Returns:
            List of discovery entries with metadata
            
        Raises:
            MemoryError: If retrieval fails
        """
        try:
            if filter_func:
                if not callable(filter_func):
                    raise ValueError("filter_func must be callable")
                return [entry for entry in self._memory if filter_func(entry)]
                
            return self._memory.copy()
            
        except Exception as e:
            logger.error(f"Failed to retrieve memory: {str(e)}")
            raise MemoryError(f"Retrieval failed: {str(e)}") from e

    def clear_memory(self) -> None:
        """Clear all stored discoveries"""
        self._memory.clear()
        logger.info("Memory store cleared")

    def _handle_capacity_limit(self) -> None:
        """Handle memory capacity limit"""
        # Implement your preferred strategy:
        # 1. Remove oldest entries
        # 2. Throw error
        # 3. Compress data
        # Here we use FIFO removal
        removed = self._memory.pop(0)
        logger.warning(
            f"Memory capacity reached, removed oldest entry: "
            f"{self._truncate_repr(removed['discovery'])}"
        )

    def _truncate_repr(self, obj: Any, max_len: int = 100) -> str:
        """Create truncated string representation of an object"""
        s = str(obj)
        return s[:max_len] + ('...' if len(s) > max_len else '')
    
    def remove_discovery(
        self,
        discovery: Optional[str] = None,
        metadata_key: Optional[str] = None,
        metadata_value: Optional[Any] = None
    ) -> None:
        """
        Remove discoveries based on specific criteria.

        Args:
            discovery: The value of the discovery to remove.
            metadata_key: The metadata key to match.
            metadata_value: The metadata value to match.

        Raises:
            ValueError: If no valid criteria are provided.
            MemoryError: If removal fails.
        """
        try:
            if not discovery and not (metadata_key and metadata_value):
                raise ValueError("Must provide either discovery or metadata key-value pair")

            # Create a copy of the memory to avoid modifying it during iteration
            memory_copy = self._memory.copy()

            # Remove entries that match the criteria
            for entry in memory_copy:
                if (discovery and entry["discovery"] == discovery) or (
                    metadata_key and metadata_value
                    and entry["metadata"].get(metadata_key) == metadata_value
                ):
                    self._memory.remove(entry)
                    logger.info(f"Removed discovery: {self._truncate_repr(entry['discovery'])}")

        except Exception as e:
            logger.error(f"Failed to remove discovery: {str(e)}")
            raise MemoryError(f"Removal failed: {str(e)}") from e

    def __repr__(self) -> str:
        """Official string representation of the MemoryStore"""
        return (f"MemoryStore(size={len(self._memory)}/"
                f"{self._max_size}, "
                f"oldest={self._memory[0]['timestamp'] if self._memory else 'None'})")