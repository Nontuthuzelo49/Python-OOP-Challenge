class Pet:
    def __init__(self, name, pet_type="Dog"):
        """
        Constructor to initialize the pet's attributes.
         param name: Name of the pet
        """
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5  # Initial hunger level (0 = full, 10 = very hungry)
        self.energy = 5  # Initial energy level (0 = tired, 10 = fully rested)
        self.happiness = 5  # Initial happiness level (0–10)
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """
        Reduces hunger by 3 points (but not below 0) and increases happiness by 1.
        """
        print(f"{self.name} 🍗 is eating...")
        self.hunger = max(self.hunger - 3, 0)  # Decrease hunger but not below 0
        self.happiness = min(self.happiness + 1, 10)  # Increase happiness but not above 10

    def sleep(self):
        """
        Increases energy by 5 points (but not above 10).
        """
        print(f"{self.name} 😴 is sleeping...")
        self.energy = min(self.energy + 5, 10)  # Increase energy but not above 10

    def play(self):
        """
        Decreases energy by 2, increases happiness by 2, and increases hunger by 1.
        """
        if self.energy > 0:  # Ensure the pet has enough energy to play
            print(f"{self.name} 🐶 is playing...") if self.pet_type == "dog" else print(f"{self.name} 🐱 is playing...")
            self.energy = max(self.energy - 2, 0)  # Decrease energy but not below 0
            self.happiness = min(self.happiness + 2, 10)  # Increase happiness but not above 10
            self.hunger = min(self.hunger + 1, 10)  # Increase hunger but not above 10
        else:
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        """
        Teaches the pet a new trick and stores it in a list.
        """
        print(f"{self.name} is learning a new trick: {trick}")
        self.tricks.append(trick)

    def show_tricks(self):
        """
        Prints all the tricks the pet has learned.
        """
        if self.tricks:
            print(f"{self.name}'s learned tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        """
        Prints the current state of the pet.
        """
        emoji = "🐶" if self.pet_type == "dog" else "🐱" if self.pet_type == "cat" else "🐦"
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger} 🍕")
        print(f"Energy: {self.energy} ⚡")
        print(f"Happiness: {self.happiness} 😊")
        print("Tricks:", self.tricks if self.tricks else "No tricks learned yet.")
   # Custom Actions
    def bath(self):
        """
        Gives the pet a bath, increasing happiness by 3.
        """
        print(f"{self.name} 🛁 is taking a bath...")
        self.happiness = min(self.happiness + 3, 10)

    def walk(self):
        """
        Takes the pet for a walk, decreasing energy by 1 and increasing happiness by 2.
        """
        if self.energy > 0:
            print(f"{self.name} 🚶‍♂️  is going for a walk...")
            self.energy = max(self.energy - 1, 0)
            self.happiness = min(self.happiness + 2, 10)
        else:
            print(f"{self.name} 💤 is too tired to go for a walk!")