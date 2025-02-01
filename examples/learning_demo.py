from mosaic.learning import MemoryStore, MemoryError, logger
# Create an instance of MemoryStore with a maximum capacity of 5 entries
memory_store = MemoryStore(max_size=5)

# Store discoveries with optional metadata
try:
    memory_store.store_discovery("Discovery 1: Quantum Entanglement", {"category": "Physics"})
    memory_store.store_discovery("Discovery 2: Black Holes", {"category": "Astronomy"})
    memory_store.store_discovery("Discovery 3: DNA Structure", {"category": "Biology"})
    memory_store.store_discovery("Discovery 4: Artificial Intelligence", {"category": "Computer Science"})
    memory_store.store_discovery("Discovery 5: Renewable Energy", {"category": "Environmental Science"})
    # This will trigger the capacity limit handling
    memory_store.store_discovery("Discovery 6: CRISPR Technology", {"category": "Genetics"})
except MemoryError as e:
    logger.error(f"Error storing discovery: {e}")

# Retrieve all stored discoveries
try:
    all_discoveries = memory_store.retrieve_memory()
    print("All Discoveries:")
    for entry in all_discoveries:
        print(f"- {entry['discovery']} (Timestamp: {entry['timestamp']}, Metadata: {entry['metadata']})")
except MemoryError as e:
    logger.error(f"Error retrieving memory: {e}")

# Retrieve discoveries filtered by category "Physics"
try:
    physics_discoveries = memory_store.retrieve_memory(
        filter_func=lambda entry: entry['metadata'].get('category') == 'Physics'
    )
    print("\nPhysics Discoveries:")
    for entry in physics_discoveries:
        print(f"- {entry['discovery']}")
except MemoryError as e:
    logger.error(f"Error retrieving filtered memory: {e}")

# Clear all stored discoveries
memory_store.clear_memory()

# Verify that the memory store is empty
try:
    empty_memory = memory_store.retrieve_memory()
    print("\nMemory after clearing:", empty_memory)
except MemoryError as e:
    logger.error(f"Error retrieving memory after clearing: {e}")