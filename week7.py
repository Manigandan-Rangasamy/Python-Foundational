# Class and Objects 

# Objects
x = 123

print(type(x))

def hello_world():
    print("hello")

print(type(hello_world))


# object methods
x = 1 
y = "two"

print(x+y)

x = 1 
y = 2

print(x+y)

name  = "mani"

print(name.upper())

x = 1 

print(x.upper())


"""
### Introduction to OOP: Classes and Objects

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to model real-world entities. It allows developers to organize code in a way that is more modular, reusable, and easier to maintain.

---

### Classes and Objects

- **Class**: A blueprint for creating objects (instances). It defines a set of attributes and methods that the created objects will have.

- **Object**: An instance of a class. It is a concrete entity based on the class blueprint.

#### Example of a Class and Object:
"""

# Example of a Class and Object
class Dog:
    # Class attribute
    species = "Canis lupus familiaris"

    # Constructor method
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

# Creating an object (instance) of the Dog class
my_dog = Dog("Buddy", 5)

# Accessing attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
print(my_dog.bark())  # Output: Buddy says woof!

"""
### Attributes, Methods, and Constructors

- **Attributes**: Variables that hold data associated with a class and its objects. They can be of two types:
  - **Instance Attributes**: Data unique to each instance (object) of the class.
  - **Class Attributes**: Data shared among all instances of a class.

- **Methods**: Functions defined inside a class that describe the behaviors of the objects created from the class. There are different types of methods:
  - **Instance Methods**: Operate on an instance of the class and can access both instance and class attributes.
  - **Class Methods**: Operate on the class itself, rather than any particular instance. They are marked with the `@classmethod` decorator.
  - **Static Methods**: Don’t modify class or instance state. They are marked with the `@staticmethod` decorator.

- **Constructor**: A special method called `__init__()` in Python, used to initialize objects when they are created.

#### Example Demonstrating Attributes, Methods, and Constructor:
"""

# Example Demonstrating Attributes, Methods, and Constructor
class Car:
    # Class attribute
    wheels = 4

    # Constructor method
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

    # Instance method
    def start_engine(self):
        return f"{self.brand} {self.model} engine started."

    # Class method
    @classmethod
    def set_wheels(cls, number):
        cls.wheels = number

    # Static method
    @staticmethod
    def honk_horn():
        return "Honk! Honk!"

# Creating an object (instance) of the Car class
my_car = Car("Toyota", "Corolla")

# Accessing attributes and methods
print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.start_engine())  # Output: Toyota Corolla engine started.
print(Car.wheels)  # Output: 4

# Using class method
Car.set_wheels(6)
print(Car.wheels)  # Output: 6

# Using static method
print(Car.honk_horn())  # Output: Honk! Honk!

"""
### Important Points to Remember:
1. **Class**: Blueprint for objects, defines attributes and methods.
2. **Object**: Instance of a class, has unique data defined by the class.
3. **Attributes**: Variables that hold data, can be instance-specific or shared among all instances (class attributes).
4. **Methods**: Functions that describe the behavior of the objects. Include instance methods, class methods, and static methods.
5. **Constructor (`__init__`)**: Special method used for initializing objects when they are created.

These concepts form the foundation of OOP, allowing for better code organization, reuse, and scalability.
"""

### Encapsulation and Abstraction: Core Concepts in OOP

"""

Encapsulation and abstraction are fundamental principles of Object-Oriented Programming (OOP). They help manage complexity and improve code organization, making your programs more modular, maintainable, and secure.

---

### Encapsulation

**Encapsulation** is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit called a class. Encapsulation also involves restricting direct access to some of an object’s components, which is a means of preventing accidental interference and misuse of the data.

#### Key Aspects:
- Private and Public Access: Encapsulation allows you to control the visibility and accessibility of the class members (attributes and methods). 
  - Private Members: These are hidden from outside the class and are not accessible directly. In Python, private members are typically indicated by prefixing the name with an underscore (_) or double underscore (__).
  - Public Members: These are accessible from outside the class.
  
- Getter and Setter Methods: These methods allow controlled access to the private attributes. The getter method returns the attribute value, while the setter method updates it.
"""

# Example of Encapsulation
class Employee:
    def __init__(self, name, salary):
        self.name = name       # Public attribute
        self.__salary = salary  # Private attribute

    # Getter method for salary
    def get_salary(self):
        return self.__salary

    # Setter method for salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

# Creating an object
emp = Employee("John Doe", 50000)

# Accessing public attribute
print(emp.name)  # Output: John Doe

# Accessing private attribute via getter method
print(emp.get_salary())  # Output: 50000

# Modifying private attribute via setter method
emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000

"""
### Accessing Private Attributes in Python

In Python, the concept of "private" attributes is not enforced as strictly as in some other programming languages. 
Python uses a convention called "name mangling" to make private attributes harder to access, but it does not prevent access entirely.

---

### Explanation:

- **Name Mangling**: 
  - When you prefix an attribute with double underscores (e.g., `__salary`), Python internally "mangles" the name to make it less accessible from outside the class. 
  However, it is still possible to access it if you know the mangled name.

- **Mangled Name**:
  - The name is changed internally to `_ClassName__attributeName`. 
  For example, if you have a class `Employee` with a private attribute `__salary`, Python internally renames it to `_Employee__salary`.

#### Example:
"""

# Example showing how private attributes can be accessed using name mangling
class Employee:
    def __init__(self, name, salary):
        self.name = name       # Public attribute
        self.__salary = salary  # Private attribute (name-mangled)

# Creating an instance of Employee
emp = Employee("John Doe", 50000)

# Accessing private attribute directly using the mangled name
print(emp._Employee__salary)  # Output: 50000

"""
### Why Use Getter and Setter Methods?

Even though you can access the mangled name of the private attribute, it is considered a best practice to use getter and setter methods:

- **Encapsulation**: Getter and setter methods help encapsulate the internal state of the object, providing a controlled way to access and modify the data.
- **Validation and Logic**: Setters allow you to add validation or other logic when changing an attribute's value. For example, you can ensure that a salary is always positive before updating it.

### Summary:

- Python's "private" attributes are not truly private but are name-mangled to discourage accidental access.
- You can still access these attributes using their mangled names, but it's generally discouraged.
- Using getter and setter methods is a way to adhere to encapsulation and allows for validation and controlled access to private attributes.
"""


"""
**Benefits of Encapsulation**:
- Data Protection: Encapsulation helps protect an object's internal state by controlling how the data is accessed and modified.
- Modularity: It allows you to change the internal implementation of the class without affecting the code that uses the class.
- Ease of Maintenance: Encapsulated code is easier to understand and maintain.

"""

# Abstraction

"""
Abstraction is like using something without needing to understand how it works inside. Let's use the example of a TV remote to understand this concept.

---

**Imagine a TV Remote:**

- You have a TV remote with buttons to change channels, increase the volume, and turn the TV on or off.
- When you press the "volume up" button, the TV gets louder, and when you press the "channel up" button, the TV changes to the next channel.
- You don't need to know how the remote sends signals to the TV, how the TV processes those signals, or how the sound gets louder. 
You just know that pressing the buttons makes things happen.

"""

# Example showing abstraction using a TV Remote

class TVRemote:
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")

    def volume_up(self):
        print("Volume increased")

    def volume_down(self):
        print("Volume decreased")

    def change_channel(self, channel_number):
        print(f"Channel changed to {channel_number}")

# Using the TVRemote
remote = TVRemote()

# You only need to know which buttons to press to use the remote
remote.turn_on()         # Output: TV is now ON
remote.volume_up()       # Output: Volume increased
remote.change_channel(5) # Output: Channel changed to 5
remote.turn_off()        # Output: TV is now OFF

"""
### How This Shows Abstraction:

- When you use the `TVRemote`, you don't worry about how the remote works inside. You only care about pressing buttons to get the desired result.
- The complicated parts of sending signals, increasing volume, and changing channels are hidden (abstracted) from you. You just use the remote without needing to understand the details.

This is what abstraction is all about: hiding the complex details and providing a simple way to interact with something.
"""


"""
**Benefits of Abstraction**:
- Simplified Interface: Users interact with the system through a simple interface that hides the complex details.
- Focus on Essentials: Abstraction allows the user to focus on the essentials without worrying about the underlying implementation.
- Enhanced Flexibility: By separating the interface from the implementation, abstraction allows changes to the implementation without affecting users.

---

### Summary

- **Encapsulation** is about bundling the data and the methods that manipulate the data, and restricting access to the inner workings of the class to protect the integrity of the data.
- **Abstraction** is about simplifying complex reality by modeling classes appropriate to the problem, and working at the level of interaction that is most useful, without needing to consider the complexity underneath.

Together, encapsulation and abstraction help in building systems that are easier to understand, maintain, and extend.

---
"""
### Static Methods and Class Methods
"""
In Python, static methods and class methods are types of methods that belong to a class rather than instances of the class. 
They are useful in different scenarios, depending on whether the method needs to interact with class-level data or doesn't need to interact with any data specific to an instance.

### 1. Static Methods

A **static method** is a method that doesn’t operate on an instance of the class (i.e., it doesn’t take self as its first argument). Static methods are often used for utility functions that perform a task in isolation, without needing to access or modify the class or instance-specific attributes.

"""

# Example of a Static Method
class MathUtils:
    @staticmethod
    def add_numbers(x, y):
        return x + y

    @staticmethod
    def multiply_numbers(x, y):
        return x * y

# Using static methods without creating an instance
result1 = MathUtils.add_numbers(5, 7)
result2 = MathUtils.multiply_numbers(3, 4)

print(f"Addition: {result1}")   # Output: Addition: 12
print(f"Multiplication: {result2}")  # Output: Multiplication: 12

"""
### 2. Class Methods

A **class method** is a method that is bound to the class rather than an instance of the class. It takes cls as its first argument, which refers to the class itself. Class methods can be used to modify class-level attributes or perform actions related to the class as a whole.

"""

# Example of a Class Method
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Class method
    @classmethod
    def set_wheels(cls, number):
        cls.wheels = number

    # Instance method
    def display_info(self):
        return f"Car: {self.brand} {self.model}, Wheels: {Car.wheels}"

# Changing the number of wheels using class method
Car.set_wheels(6)

# Creating instances
car1 = Car("Tesla", "Model S")
car2 = Car("Ford", "Mustang")

# Displaying information
print(car1.display_info())  # Output: Car: Tesla Model S, Wheels: 6
print(car2.display_info())  # Output: Car: Ford Mustang, Wheels: 6

"""
### Summary:
- **Static Methods**:
  - Defined using `@staticmethod`.
  - Do not take `self` or `cls` as the first argument.
  - Used for utility functions that do not depend on the class or instance state.

- **Class Methods**:
  - Defined using `@classmethod`.
  - Take `cls` as the first argument, representing the class.
  - Used to manipulate class-level data or perform operations related to the class itself, rather than instances.

These concepts are powerful tools for creating well-structured and flexible code in object-oriented programming.
"""
