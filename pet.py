import sys
sys.stdout.reconfigure(encoding='utf-8')

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # (Other members' methods stay here - DON'T TOUCH)

    def get_status(self):
        """Display pet's status with emoji bars"""
        print(f"\n📊 {self.name}'s Status:")
        print(f"Hunger:    [{'🍕' * self.hunger}{'⬜' * (10 - self.hunger)}] {self.hunger}/10")
        print(f"Energy:    [{'⚡' * self.energy}{'⬜' * (10 - self.energy)}] {self.energy}/10")
        print(f"Happiness: [{'❤️' * self.happiness}{'⬜' * (10 - self.happiness)}] {self.happiness}/10")
        
        # Warnings
        if self.hunger >= 8:
            print("⚠️ Feed me! (Hunger ≥ 8)")
        if self.energy <= 2:
            print("⚠️ Zzz... I need sleep! (Energy ≤ 2)")
        if self.happiness <= 2:
            print("⚠️ Play with me! (Happiness ≤ 2)")

    def train(self, trick):
        """Teach a new trick (case-insensitive)"""
        if not isinstance(trick, str):
            print("❌ Trick must be a string!")
            return

        trick = trick.strip().title()
        if trick.lower() in [t.lower() for t in self.tricks]:
            print(f"🐾 {self.name} already knows '{trick}'!")
        else:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"🎉 {self.name} learned '{trick}'!")

    def show_tricks(self):
        """Show all tricks with numbering"""
        if not self.tricks:
            print(f"📭 {self.name} knows no tricks yet.")
        else:
            print(f"\n📜 {self.name}'s Tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick} 🎯")

    
    def __str__(self):
        return f"{self.name} is an amazing pet."
    

# pet = Pet("Fluffy")
# pet.train("Roll Over")
# pet.train("Play Dead")
# pet.train("Run")
# pet.show_tricks()
# pet.get_status()