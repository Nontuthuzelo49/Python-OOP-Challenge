class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level
        self.energy = 7  # Default energy level
        self.happiness = 6  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} just ate and feels happier! Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap! Energy: {self.energy}")