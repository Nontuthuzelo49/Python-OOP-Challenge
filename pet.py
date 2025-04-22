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
        return f"{self.name} is eating... Yum!"
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        return f"{self.name} is sleeping... Zzz"
    
    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        return f"{self.name} is playing... Woo!"
    
    def get_status(self):
        return f"""
{self.name}'s Status:
Hunger: {self.hunger}/10
Energy: {self.energy}/10
Happiness: {self.happiness}/10
"""
    
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)
            self.happiness = min(10, self.happiness + 1)
            return f"{self.name} learned to {trick}!"
        return f"{self.name} already knows how to {trick}!"
    
    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet!"
        return f"{self.name}'s tricks: {', '.join(self.tricks)}"
