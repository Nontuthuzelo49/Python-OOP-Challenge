class Pet:
    # Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name  # Name of the pet
        self.hunger = 15  # Hunger level (higher means hungrier)
        self.energy = 10  # Energy level
        self.happiness = 20  # Happiness level
        self.tricks = []  # List of tricks the pet knows

    def eat(self):
        pass

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} is sleeping. Energy is now {self.energy}.")

    def play(self):
        pass

    def train(self, trick):
        pass

    def show_tricks(self):
        pass

    def get_status(self):
        pass

