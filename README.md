# Virtual Pet Simulator

A simple Python-based virtual pet simulator where you can create and interact with a digital pet. This project demonstrates object-oriented programming concepts in Python.

## Features

- Create a pet with a custom name
- Basic pet care actions:
  - Feeding
  - Playing
  - Sleeping
- Status tracking:
  - Hunger level
  - Energy level
  - Happiness level
- Trick training system
- Status monitoring

## How to Run

1. Make sure you have Python installed on your system
2. Clone this repository
3. Run the main program:
```bash
python main.py
```

## Class Structure

The project consists of two main files:
- `pet.py`: Contains the Pet class with all pet-related functionality
- `main.py`: Demo program showing how to use the Pet class

## Example Usage

```python
my_pet = Pet("Buddy")
my_pet.eat()        # Feed your pet
my_pet.play()       # Play with your pet
my_pet.sleep()      # Let your pet rest
my_pet.train("sit") # Teach your pet a new trick
```

## Status System

Each pet has three main status attributes:
- Hunger (0-10)
- Energy (0-10)
- Happiness (0-10)

These values change based on the activities you do with your pet.

## Author

Connect with me on LinkedIn: [Almando](https://www.linkedin.com/in/almando/)

## Contributors

- [Milon Odhiambo](https://github.com/Miltonnare)

## License

This project is free to use and modify.