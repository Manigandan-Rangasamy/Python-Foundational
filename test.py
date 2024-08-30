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

emp.__salary = 90000

print(emp.__salary)