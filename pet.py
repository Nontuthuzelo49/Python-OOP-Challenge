class Pet:
    
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # A function to reduce hunger by 3 points (but not below 0), and increases happiness by 1.
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating!")

    # A function to increase energy by 5 points (but not above 10).
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping!")

    # A function to decrease energy by 2, increase happiness by 2, and hunger by 1.
    def play(self):
        if( self.energy <= 0):
            print(f"{self.name} is tired and can't play!")
            return
        else:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")

    # A function that teaches your pet a new trick and stores it in a list.
    def train(self, trick):
        self.tricks.append(trick)

    # A function that shows the tricks your pet has learned..
    def show_tricks(self):
        print(f"{self.name} knows these tricks: {self.tricks}")

    # A function that print the current state of the pet.
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")









