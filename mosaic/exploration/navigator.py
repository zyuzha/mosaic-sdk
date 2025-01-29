class Navigator:
    def __init__(self):
        self.current_location = "Starting Point"

    def explore(self):
        # Logic for exploring new areas in the simulation.
        self.current_location = "New Realm"
        print(f"Exploring: {self.current_location}")

    def get_current_location(self):
        return self.current_location
