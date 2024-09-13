"""
### Inheritance 

Inheritance allows a class (child class) to "inherit" attributes and methods from another class (parent class). 
This makes it easy to create new classes without writing repetitive code.

---

**Imagine Vehicles:**

- Let's say you have a general class `Vehicle` that represents any kind of vehicle (like cars, bikes, or trucks).
- A `Car` class can inherit from `Vehicle`, which means it will have all the characteristics of a vehicle, but with additional details specific to cars.

---

**In Code:**
"""

# Parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Vehicle's make
        self.model = model  # Vehicle's model

    def describe(self):
        return f"This is a {self.make} {self.model}."

# Child class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Inherit attributes from Vehicle
        self.doors = doors  # Additional attribute specific to Car

    def car_details(self):
        return f"It is a {self.doors}-door car."

# Creating an object of Car class
my_car = Car("Toyota", "Corolla", 4)

# Using the inherited method from Vehicle
print(my_car.describe())  # Output: This is a Toyota Corolla.

# Using the method specific to Car
print(my_car.car_details())  # Output: It is a 4-door car.

"""
### How This Shows Inheritance:

- The `Car` class inherits attributes and methods from the `Vehicle` class (like `make` and `model` and the `describe()` method).
- The `Car` class adds its own attribute `doors` and its own method `car_details()`.
- Inheritance helps in building specialized classes (like `Car`) that reuse code from general classes (like `Vehicle`), making programming more efficient and less repetitive.
"""

"""
### Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common parent class. 
The same method behaves differently based on the object that calls it.

---

**Imagine Musical Instruments:**

- Let's say we have different musical instruments, like `Guitar` and `Drum`. Both instruments can play music, but each plays a different type of sound.
- We can have a `play_sound()` method that works differently depending on whether it's a guitar or drum.

---

**In Code:**
"""

# Parent class
class Instrument:
    def play_sound(self):
        raise NotImplementedError("Subclass must implement this method")

# Guitar class inherits from Instrument
class Guitar(Instrument):
    def play_sound(self):
        return "Strumming guitar sounds!"

# Drum class inherits from Instrument
class Drum(Instrument):
    def play_sound(self):
        return "Beating drum sounds!"

# Function to demonstrate polymorphism
def start_music(instrument):
    return instrument.play_sound()

# Creating objects of Guitar and Drum
guitar = Guitar()
drum = Drum()

# Using the same method but different results based on the object
print(start_music(guitar))  # Output: Strumming guitar sounds!
print(start_music(drum))    # Output: Beating drum sounds!

"""
### How This Shows Polymorphism:

- Both `Guitar` and `Drum` are musical instruments, but they play different sounds.
- The `play_sound()` method behaves differently depending on whether a `Guitar` or `Drum` object is calling it.
- This allows us to use the same method (`play_sound`) on different instruments while getting different results.
"""
