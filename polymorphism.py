# Base class
class Entity:
    def move(self):
        """Define a generic move method."""
        raise NotImplementedError("Subclasses must implement this method!")

# Animal classes
class Dog(Entity):
    def move(self):
        """Dog's specific movement."""
        return "Running 🐕"

class Fish(Entity):
    def move(self):
        """Fish's specific movement."""
        return "Swimming 🐟"

class Bird(Entity):
    def move(self):
        """Bird's specific movement."""
        return "Flying 🐦"

# Vehicle classes
class Car(Entity):
    def move(self):
        """Car's specific movement."""
        return "Driving 🚗"

class Plane(Entity):
    def move(self):
        """Plane's specific movement."""
        return "Flying ✈️"

class Boat(Entity):
    def move(self):
        """Boat's specific movement."""
        return "Sailing 🚤"

# Polymorphism in action
def show_movement(entities):
    """Display how each entity moves."""
    for entity in entities:
        print(f"{entity.__class__.__name__}: {entity.move()}")

# Create objects of animals and vehicles
entities = [
    Dog(),
    Fish(),
    Bird(),
    Car(),
    Plane(),
    Boat()
]

# Show how each entity moves
if __name__ == "__main__":
    show_movement(entities)
