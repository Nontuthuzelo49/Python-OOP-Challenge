from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Buddy")
    
    # Test basic actions
    print(my_pet.get_status())
    print(my_pet.eat())
    print(my_pet.play())
    print(my_pet.sleep())
    print(my_pet.get_status())
    
    # Test tricks
    print(my_pet.train("sit"))
    print(my_pet.train("roll over"))
    print(my_pet.train("sit"))  # Try to teach the same trick
    print(my_pet.show_tricks())
    print(my_pet.get_status())

if __name__ == "__main__":
    main()
