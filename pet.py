class myPet:
    def __init__(self):
        self.name =input("Enter the name of our pet: ")
        self.hunger = 10
        self.energy = 0
        self.happiness = 2

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten. Hunger is now {self.hunger}. Happiness is {self.happiness}.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy is now {self.energy}.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and is now happier!")
        else:
            print(f"{self.name} is too tired to play. Try letting them sleep.")

    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}\n")

