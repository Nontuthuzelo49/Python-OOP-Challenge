class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default value (moderate hunger)
        self.energy = 5  # Default value (moderate energy)
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Ensure hunger doesn't go below 0
        self.happiness = min(10, self.happiness + 1)  # Ensure happiness doesn't exceed 10
        print(f"{self.name} ate and feels happier!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Ensure energy doesn't exceed 10
        print(f"{self.name} is well-rested!")

    def play(self):
        if self.energy >= 2:  # Check if there's enough energy to play
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and is feeling happy!")
        else:
            print(f"{self.name} is too tired to play. Let them rest first.")

    def get_status(self):
        print(f"\n📊 **{self.name}'s Status**:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    # Bonus Methods 🎯
    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)  # Training makes pets happier
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Example usage:
my_pet = Pet("Freya")
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("Roll over")
my_pet.show_tricks()
