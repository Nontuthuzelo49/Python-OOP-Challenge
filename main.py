from pet import Pet

# Create a new pet object
print("Creating pet: Dog")
dog = Pet("Leo", pet_type="dog")

#dog the pet's methods
dog.eat()
dog.play()
dog.sleep()

#dog the pet some tricks
dog.train("roll over")
dog.train("play dead")

#dog the pet's tricks
dog.show_tricks()

# Custom actions
dog.bath()
dog.walk()

#dog he pet's current status
dog.get_status()