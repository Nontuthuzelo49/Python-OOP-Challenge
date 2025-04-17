from pet import Pet

def main():
    my_dog = Pet("Sophie")

    my_dog.get_status()
    my_dog.eat()
    my_dog.sleep()
    my_dog.play()
    my_dog.get_status()

    my_dog.train("jumping")
    my_dog.train("running")
    my_dog.show_tricks()

if __name__ == "__main__":
    main()

