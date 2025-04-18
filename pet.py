class Pet:
    def __init__(self, name):
        # Initialize the pet with a name and default attribute values.
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # Reduce hunger and increase happiness when the pet eats.
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily!🍗")

    def sleep(self):
        # Increase energy when the pet sleeps.
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is now sleeping...😴")

    def play(self):
        # Play with the pet if it has enough energy.
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays around with me!🐕")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        # Teach the pet a new trick if it doesn't already know it.
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows that trick.")

    def show_tricks(self):
        # Display all the tricks the pet knows.
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        # Display the pet's current status with a fun banner.
        print(" ")
        print("  ⭐⭐⭐⭐⭐")
        print(f"🐶 {self.name}'s current status:")
        print(f"  Hunger level: {self.hunger}/10")
        print(f"  Energy level: {self.energy}/10")
        print(f"  Happiness level: {self.happiness}/10")
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily!🍗")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is now sleeping...😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays around with me!🐕")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(" ")
        print("  ⭐⭐⭐⭐⭐")
        print(f"🐶 {self.name}'s current status:")
        print(f"  Hunger level: {self.hunger}/10")
        print(f"  Energy level: {self.energy}/10")
        print(f"  Happiness level: {self.happiness}/10")
