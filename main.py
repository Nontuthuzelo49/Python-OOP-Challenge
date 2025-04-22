from pet import myPet

mypet = myPet()

while True:
    print("What do you want to do?")
    print("1. Feed the pet")
    print("2. Take pet to sleep")
    print("3. Play with pet")
    print("4. Get status")
    print("5. Exit")

    choice = input("Pick a choice from the above: ")

    if choice == "1":
        mypet.eat()
    elif choice == "2":
        mypet.sleep()
    elif choice == "3":
        mypet.play()
    elif choice == "4":
        mypet.get_status()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice. Try again.")        
