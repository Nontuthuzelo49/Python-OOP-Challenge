
# In main.py (or you can run it here):
my_pet = Pet("Buddy")

# Demonstrate basic interactions
print(" Basic Interactions ")
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.get_status()

# Demonstrate training tricks
print("\n Training Tricks ")
my_pet.train("roll over")
my_pet.train("fetch")
my_pet.train("speak")
my_pet.show_tricks()

# Show status after training
print("\n Final Status: ")
my_pet.get_status()