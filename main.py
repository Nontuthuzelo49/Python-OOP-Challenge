from pet import Pet

# Create a new pet object
print("Creating pet: Dog")
dog = Pet("Leo", pet_type="dog")

# Dog does the pet's methods
dog.eat()
dog.play()
dog.sleep()

# Teach the dog some tricks
dog.train("roll over")
dog.train("play dead")

# Show the dog's tricks
dog.show_tricks()

# Custom actions
dog.bath()
dog.walk()

# Show the dog's current status
dog.get_status()
