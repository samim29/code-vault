"""#### 5.Design classes representing a House and its various components like Bedroom, LivingRoom, and Kitchen. 
Implement composition by creating a House object that contains instances of its components."""
class Bedroom:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} (Size: {self.size} sq ft)"

class LivingRoom:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Living Room (Size: {self.size} sq ft)"

class Kitchen:
    def __init__(self, size, appliances):
        self.size = size
        self.appliances = appliances

    def __str__(self):
        appliances_str = ", ".join(self.appliances)
        return f"Kitchen (Size: {self.size} sq ft, Appliances: {appliances_str})"

class House:
    def __init__(self, address, bedrooms, living_room, kitchen):
        self.address = address
        self.bedrooms = bedrooms
        self.living_room = living_room
        self.kitchen = kitchen

    def __str__(self):
        bedroom_str = "\n".join(str(bedroom) for bedroom in self.bedrooms)
        return f"House at {self.address}:\n{bedroom_str}\n{self.living_room}\n{self.kitchen}"

# Example usage
def main():
    # Create the components of the house
    bedroom1 = Bedroom("Master Bedroom", 250)
    bedroom2 = Bedroom("Guest Bedroom", 180)
    living_room = LivingRoom(400)
    kitchen = Kitchen(150, ["Stove", "Refrigerator", "Dishwasher"])

    # Create the house
    house = House("123 Main Street Banglore IN", [bedroom1, bedroom2], living_room, kitchen)

    # Print the house information
    print(house)

if __name__ == "__main__":
    main()
