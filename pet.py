class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0  
        self.energy = 10  
        self.happiness = 5  
        self.tricks = []  

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  
        self.happiness = min(10, self.happiness + 1)  
        print(f"{self.name} is eating. Hunger reduced, happiness increased!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  
        print(f"{self.name} is sleeping. Energy restored!")

    def play(self):
        if self.energy >= 2:  
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)  
            self.hunger = min(10, self.hunger + 1) 
            print(f"{self.name} is playing. Energy decreased, happiness and hunger increased!")
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        if self.energy >= 3: 
            self.energy -= 3
            self.happiness = min(10, self.happiness + 1) 
            self.tricks.append(trick)
            print(f"{self.name} is training. Learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to train!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

my_pet = Pet("KIRSTY")

my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.train("roll over")
my_pet.show_tricks()
my_pet.get_status()
