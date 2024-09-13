"""
### Simple Calculator Project with User Input

This project demonstrates the use of a simple class to perform basic calculator operations
like addition, subtraction, multiplication, and division. The user provides the inputs.

---

#### Key Features:
- A `Calculator` class with methods for adding, subtracting, multiplying, and dividing two numbers.
- Takes user input for the operation and numbers.
"""

# Simple Calculator class
class Calculator:
    
    # Method to add two numbers
    def add(self, a, b):
        return a + b

    # Method to subtract the second number from the first
    def subtract(self, a, b):
        return a - b

    # Method to multiply two numbers
    def multiply(self, a, b):
        return a * b

    # Method to divide the first number by the second
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

# Function to get user input and perform calculations
def calculator_with_input():
    calc = Calculator()

    while True:
        # Ask the user for input
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if choice == '5':
            print("Exiting the calculator.")
            break

        # Ask for two numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the operation based on user choice
        if choice == '1':
            print(f"Result: {num1} + {num2} = {calc.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {calc.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {calc.multiply(num1, num2)}")
        elif choice == '4':
            result = calc.divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please choose a valid operation.")

# Run the calculator with user input
calculator_with_input()
