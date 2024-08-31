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

print(emp._Employee__salary)