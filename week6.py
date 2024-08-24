# Python Exceptions

"""

Exceptions in Python are events that occur during the execution of a program that disrupt the normal flow of instructions. 
They are typically errors that happen due to various reasons like invalid input, file not found, division by zero, etc. 
When such an error occurs, Python raises an exception, which is a signal that something unexpected has happened.
"""
# Exceptions vs. Errors
#Error (Compile time)
# print("Hello World" 

# Logical Error
a = 15
b = 10

divide = a + b
print(divide)

# Runtime Error
result = 10 / 0

# Importance of Exception Handling
"""
Prevent Crashes: By handling exceptions, you can prevent your program from crashing and allow it to fail gracefully.
Debugging: Exceptions provide valuable information about errors in your code, making it easier to debug.
Program Flow: Exceptions allow you to manage different error conditions, giving you control over how your program responds to unexpected situations.
"""

# Common Python Exceptions:
"""
ZeroDivisionError: Raised when trying to divide by zero.
ValueError: Raised when a function receives an argument of the right type but inappropriate value, like passing a string instead of a number.
TypeError: Raised when an operation or function is applied to an object of inappropriate type.
FileNotFoundError: Raised when trying to open a file that does not exist.
IndexError: Raised when trying to access an index that is out of range in a list or a string.
KeyError: Raised when trying to access a dictionary key that does not exist.
ImportError: Raised when an import statement has trouble trying to load a module.

"""

# Exception Handling
"""
Try Block: This is where you place the code that might raise an exception.
Except Block: If an error occurs in the try block, the except block will catch the exception and execute the code inside it.
Else Block: This block runs if no exceptions are raised in the try block.
Finally Block: This block is always executed, whether an exception is raised or not, and is often used for cleanup actions.
Raising Exceptions: You can manually raise exceptions using the raise keyword.

"""
# Basic Try-Except
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

"""
The code inside the try block attempts to divide by zero, which raises a ZeroDivisionError.
The except block catches the exception and prints an error message.
"""

# Handling Multiple Exceptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError as e:
    print(f"Invalid input! Please enter a valid number. Error: {e}")
except ZeroDivisionError as e:
    print(f"Cannot divide by zero! Error: {e}")
"""
This handles two types of exceptions: ValueError (if the input is not a number) and ZeroDivisionError (if the input is zero).
The appropriate except block is executed depending on the type of exception.
"""


# Using Else with Try-Except
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError as e:
    print(f"Cannot divide by zero! Error: {e}")
except ValueError as e:
    print(f"Invalid input! Please enter a valid number. Error: {e}")
else:
    print(f"Division successful! The result is: {result}")

"""
If no exceptions are raised in the try block, the else block is executed.
This is useful for code that should only run if everything in the try block succeeds.
"""

# Finally Block
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(f"File not found! Error: {e}")
finally:
    file.close()
    print("File has been closed.")

"""
The finally block ensures that the file is closed whether an exception occurs or not.
This is useful for resource management, such as closing files or releasing locks.
"""

# Raising Exceptions
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Access granted."

try:
    print(check_age(15))
except ValueError as e:
    print(f"Error: {e}")

"""
The check_age function raises a ValueError if the age is less than 18.
The exception is caught in the try-except block when the function is called with an invalid age.
"""

# Common exception
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError as e:
    print(f"Invalid input! Please enter a valid number. Error: {e}")
except Exception as e:
    print("Some Exception",e)

"""
Instead of specifying the type of error we can catch all the errors using "Exception". 
We can print it to find the type of Exception that was occured
"""

# Python Logging Module

"""
The logging module in Python is a powerful and flexible system for tracking events that happen during program execution. 
It allows you to log messages at different levels of importance and route these messages to different destinations (console, files, etc.).
"""

import logging

logging.basicConfig(level=logging.INFO)
logging.info('This is an info message')

# Different Logging Levels

"""
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future. #*Default level
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.

"""
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()

# Logging to a File

import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG ,filemode="w",)
logging.debug('This will be logged to the file')


# Formatting the Log Messages
# link : https://docs.python.org/3/library/logging.html#logrecord-attributes

import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('This is an info message with timestamp')


# Disabling Logging
import logging

logging.disable(logging.CRITICAL)
logging.critical('This will not be logged')


# Custom Logger
import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("custom.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s] [%(filename)s:%(lineno)d] %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# example:
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    logger.error("Error occurred",exc_info=True)