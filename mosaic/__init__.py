# mosaic/__init__.py

# Example of package-level variable
__version__ = "0.1.0"

# Importing key modules for easier access
from .connection.connector import Connector
from .exploration.navigator import Navigator
from .learning.memory_store import MemoryStore
from .community.network_api import NetworkAPI

print("Mosaic SDK initialized.")
