# main.py

from pet import Pet

def main():
    print("🐾 Welcome to the Virtual Pet Game!")
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    print(f"\nGreat! You've adopted {pet_name}.\n")

    while True:
        print("What would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Pet your pet")
        print("5. Train your pet")
        print("6. Show tricks")
        print("7. Check status")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            my_pet.pet()
        elif choice == "5":
            trick = input("What trick would you like to teach your pet? ")
            my_pet.train(trick)
        elif choice == "6":
            my_pet.show_tricks()
        elif choice == "7":
            my_pet.get_status()
        elif choice == "8":
            print(f"Goodbye! {pet_name} will miss you 🐶")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 8.")

if __name__ == "__main__":
    main()