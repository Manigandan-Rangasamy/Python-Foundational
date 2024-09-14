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

### 1. Single Inheritance

Single inheritance involves one parent class and one child class. The child class inherits from a single parent class.

Parent Class -> Child Class
"""

# Example of Single Inheritance
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

# Creating an object of the Dog class
dog = Dog()
print(dog.sound())  # Output: Bark


"""
### 2. Multiple Inheritance

Multiple inheritance occurs when a child class inherits from more than one parent class. 
The child class can access methods and attributes from all the parent classes.

Parent Class 1 -> 
                -> Child Class
Parent Class 2 ->
"""

class Father:
    def skills(self):
        return "Driving"

class Mother:
    def skills(self):
        return "Cooking"

class Child(Father, Mother):
    def all_skills(self):
        # Explicitly calling methods from both parent classes
        return f"Skills: {Father.skills(self)} and {Mother.skills(self)}"

# Creating an object of the Child class
child = Child()
print(child.all_skills())  # Output: Skills: Driving and Cooking


"""
### 3. Multilevel Inheritance

In multilevel inheritance, a class inherits from a parent class, which in turn inherits from another parent class. 
This forms a chain of inheritance.

Grandparent Class -> Parent Class -> Child Class
"""

# Example of Multilevel Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def breed(self, breed_name):
        self.breed_name = breed_name
        return f"{self.name} is a {self.breed_name}"

class Bulldog(Dog):
    def sound(self):
        return "Bulldog Barks!"

# Creating an object of the Bulldog class
bulldog = Bulldog("Max")
print(bulldog.breed("Bulldog"))  # Output: Max is a Bulldog
print(bulldog.sound())           # Output: Bulldog Barks!


"""
### 4. Hierarchical Inheritance

In hierarchical inheritance, multiple child classes inherit from the same parent class. 
Each child class has access to the methods and attributes of the parent class.

           Parent Class
           /          \
    Child Class 1   Child Class 2
"""

# Example of Hierarchical Inheritance
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating objects of Dog and Cat classes
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow


"""
### 5. Hybrid Inheritance

Hybrid inheritance is a combination of two or more types of inheritance. 
It can involve any combination of the other inheritance types, such as multiple and multilevel inheritance.

Parent Class -> Child Class 1
        |       \
   Child Class 2   Child Class 3
"""

# Example of Hybrid Inheritance
class Vehicle:
    def start(self):
        return "Starting the vehicle"

class Car(Vehicle):
    def wheels(self):
        return 4

class Bike(Vehicle):
    def wheels(self):
        return 2

class Hybrid(Car, Bike):
    def wheels(self):
        return f"Hybrid vehicle has {super().wheels()} wheels"

# Creating an object of the Hybrid class
hybrid = Hybrid()
print(hybrid.start())  # Output: Starting the vehicle
print(hybrid.wheels())  # Output: Hybrid vehicle has 4 wheels

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
