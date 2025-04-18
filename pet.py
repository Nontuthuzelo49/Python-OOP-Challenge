class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 10  # Starting with moderate hunger
        self.energy = 5  # Starting with moderate energy
        self.happiness = 5  # Starting with moderate happiness
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """Reduces hunger by 3 points and increases happiness by 1"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food! Hunger decreased, happiness increased.")

    def sleep(self):
        """Increases energy by 5 points"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap! Energy increased.")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1"""
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} had fun playing! Energy decreased, happiness increased, hunger increased.")

    def get_status(self):
        """Prints the current state of the pet"""
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        """Teaches the pet a new trick"""
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}!")

    def show_tricks(self):
        """Prints all learned tricks"""
        if self.tricks:
            print(f"\n{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"\n{self.name} hasn't learned any tricks yet!")



# Creating a new pet object
my_pet = Pet("Kafka")
    
# Demonstrating the methods
my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.get_status()
    
# Demonstrating training
my_pet.train("sit")
my_pet.train("roll over")
my_pet.show_tricks()
