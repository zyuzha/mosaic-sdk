from mosaic.exploration.navigator import Navigator
from mosaic.learning.memory_store import MemoryStore

def main():
    navigator = Navigator()
    memory_store = MemoryStore()

    navigator.explore()
    memory_store.store_discovery(navigator.get_current_location())

if __name__ == "__main__":
    main()
