class MemoryStore:
    def __init__(self):
        self.memory = []

    def store_discovery(self, discovery):
        self.memory.append(discovery)
        print(f"Discovery stored: {discovery}")

    def retrieve_memory(self):
        return self.memory
