from mosaic.exploration import Navigator, ExplorationMode, NavigationError

# Initialize navigator
navigator = Navigator()

# Set exploration mode
navigator.set_exploration_mode(ExplorationMode.STEALTH)

# Explore new areas
try:
    print("Current location:", navigator.get_current_location())
    
    # Explore with direction
    new_location = navigator.explore(direction="north")
    print("New location:", new_location)
    
    # Get exploration history
    print("Exploration history:", navigator.get_exploration_history())
    
except NavigationError as e:
    print(f"Navigation error: {e}")