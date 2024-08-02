"""
Python Introduction
Python's popularity stems from its simplicity, versatility, and robustness.

Here are some of its main features:
# Readable and Simple Syntax
# Extensive Standard Library
# Dynamic Typing and Dynamic Binding
# Cross-platform Compatibility
# High-level Language
# Support for Multiple Programming Paradigms
# Large and Active Community
# Open Source

"""

# First program
print("Hello, World!")

"""
This is a multi-line comment.
You can write multiple lines of text within triple quotes.

"""

# This is a comment
# This is another comment

# Variables 
# A variable is a container for storing data

x = 10
name = "Alice"

"""
Variable names must start with a letter (a-z, A-Z) or an
underscore _.
Variable names can contain letters, digits (0-9), and
underscores _.
Variable names are case-sensitive (name and Name are
different variables).
Python keywords (e.g., if, for, while, def, etc.) cannot be
used as variable names.

"""

x = 5
x = x + 1  # x now holds the value 6

# Variable Scope
x = 10  # global variable
def my_function():
    y = 20  # local variable
    print(x)  # x can be accessed here
    print(y)  # y can be accessed here

my_function()
print(x)  # x can be accessed here
print(y)  # Error: y is not defined


# DATA TYPES

"""
Integer (int): Whole numbers, e.g., 10, -5, 1000.
Float (float): Floating-point numbers, e.g., 3.14, 2.718.
String (str): Sequence of characters, e.g., "Hello", 'Python'.
Boolean (bool): Represents True or False.
List (list), Tuple (tuple), Dictionary (dict), Set (set), etc.

"""

age = 25  # integer
pi = 3.14  # float
name = "Alice"  # string
is_student = True  # boolean


# Python boolean (True or False)

"""
Boolean values are commonly used in conditional statements, loops, and logical operations to
control the flow of the program or to represent the result of a comparison.
"""

is_student = True
has_passed_exam = False

if is_student:
    print("The person is a student.")
else:
    print("The person is not a student.")

print(bool(0))     # False
print(bool(1))     # True
print(bool([]))    # False (empty list)
print(bool([1]))   # True (non-empty list)

# Convert True to integer
boolean_value = True
integer_value = int(boolean_value)
print(integer_value)  # Output: 1
# Convert False to integer
boolean_value = False
integer_value = int(boolean_value)
print(integer_value)  # Output: 0


# Python String

# Create a variable named 'my_string' and assign a string value to it
my_string = "Hello, World!"
# Print the value of the variable
print(my_string)

# Variables in String

# Using % Operator
name = "Alice"
age = 30
graduated = True

greeting = "Hello, %s! You are %s years old." % (name, graduated)
print(greeting)

#  Using str.format() Method:

name = "Alice"
age = 30
greeting = "Hello, {}! You are {} years old.".format(name, age)
print(greeting)

# Using f-strings (Formatted String Literals): 

name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)


# Escape Sequence
"""
Escape sequences in Python strings are special characters that are preceded
by a backslash \. These sequences allow you to include characters in strings
that are difficult or impossible to type directly in source code. Here are
some commonly used escape sequences in Python:

"""
#  \n: Newline character.It inserts a newline into the string.
print("Line 1\nLine 2")

#  \t: Tab character. It inserts a horizontal tab into the string.
print("Column 1\tColumn 2")

#  \r: Carriage return character. It moves the cursor to the beginning of the line.
print("Hello\rWorld")

#  \\: Backslash character. It inserts a literal backslash into the string.
print("This is a backslash: \\")


# Using Opposite Type of Quote: 

# Using double quotes to delimit the string with single quotes inside
string_with_single_quotes = "He said, 'Hello'"
print(string_with_single_quotes)
# Using single quotes to delimit the string with double quotes inside
string_with_double_quotes = 'She said, "Hi"'
print(string_with_double_quotes)


#  Escaping Quote Characters: 
# If you want to include the same type of quote character inside a string, you can escape it using a backslash (\).

# Using single quotes with escaped single quote inside
string_with_escaped_single_quote = 'I\'m fine'
print(string_with_escaped_single_quote)
# Using double quotes with escaped double quote inside
string_with_escaped_double_quote = "She said, \"It's raining\""
print(string_with_escaped_double_quote)


# Python Integer

# Create integer variables
x = 5
y = 3
# Perform arithmetic operations
sum_result = x + y
difference_result = x - y
product_result = x * y
quotient_result = x / y  # Division returns a float in Python 3.x
floor_division_result = x // y  # Floor division returns an integer
remainder_result = x % y  # Modulus operator returns the remainder

# Print the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Floor Division:", floor_division_result)
print("Remainder:", remainder_result)

# Python Floats

# Create floating-point variables
x = 3.5
y = 2.0
# Perform arithmetic operations
sum_result = x + y
difference_result = x - y
product_result = x * y
quotient_result = x / y

# Print the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)


# Multiple Assignment

# Tuple unpacking
x, y, z = 10, 20, 30
print("x:", x)  # Output: 10
print("y:", y)  # Output: 20
print("z:", z)  # Output: 30

# List unpacking
[a, b, c] = [10, 20, 30]
print("a:", a)  # Output: 10
print("b:", b)  # Output: 20
print("c:", c)  # Output: 30

# Extended unpacking
first, *rest = [1, 2, 3, 4, 5]
print("first:", first)  # Output: 1
print("rest:", rest)    # Output: [2, 3, 4, 5]

# Swapping variables
x = 10
y = 20
x, y = y, x
print("x:", x)  # Output: 20
print("y:", y)  # Output: 10


# Convert an integer to a string
number = 123
string_number = str(number)
# Print the string representation
print(string_number)


# Convert a string to an integer
string_number = "123"
number = int(string_number)
# Print the integer value
print(number)


# Convert an integer to a floating-point number
integer_number = 123
float_number = float(integer_number)
# Print the floating-point number
print(float_number)


#Python List

"""
In Python, a list is a built-in data structure that represents a collection of
items in a specific order. Lists are mutable, meaning that you can modify
their elements after they have been created. Lists can contain elements of
different data types, and they can grow or shrink dynamically as needed.
"""

# Creating a list
my_list = [1, 2, 3, 4, 5]
# Accessing elements of the list
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
# Length of a List
length = len(my_list)
print("Length of the List:", length)
# Modifying elements of the list
my_list[1] = 10
print(my_list)  # Output: [1, 10, 3, 4, 5]
# Adding elements to the list
my_list.append(6)
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]
# Removing elements from the list
my_list.remove(3)
print(my_list)  # Output: [1, 10, 4, 5, 6]


# Define a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Access elements by index
print(my_list[0])  # Output: 'apple' (first element)
print(my_list[2])  # Output: 'cherry' (third element)
print(my_list[-1]) # Output: 'elderberry' (last element)
print(my_list[-2]) # Output: 'date' (second-to-last element)


# List Methods

# Define a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Modify elements in the list
my_list[1] = 'blueberry'  # Modify the element at index 1
my_list[-2] = 'grape'     # Modify the second-to-last element
# Print the modified list
print(my_list)  # Output: ['apple', 'blueberry', 'cherry', 'grape', 'elderberry']


# Define a list
my_list = ['apple', 'banana', 'cherry']
# Add a single element to the end of the list
my_list.append('date')
# Print the modified list
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'date']


# Define a list
my_list = ['apple', 'banana', 'cherry']
# Insert a single element at a specified index
my_list.insert(1, 'blueberry')  # Insert 'blueberry' at index 1
# Print the modified list
print(my_list)  # Output: ['apple', 'blueberry', 'banana', 'cherry']


# Define a list
my_list = ['apple', 'banana', 'cherry']
# Create another list of elements to add
new_elements = ['date', 'elderberry']
# Concatenate the two lists to add elements
my_list += new_elements
# Print the modified list
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Define a list
my_list = ['apple', 'banana', 'cherry', 'date']
# Insert an element in the middle of the list
my_list.insert(2, 'blueberry')  # Insert 'blueberry' at index 2
# Print the modified list
print(my_list)  # Output: ['apple', 'banana', 'blueberry', 'cherry', 'date']


# Define a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Sort the list permanently
my_list.sort()
# Print the sorted list
print("Sorted list:", my_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


#  Python Tuple

"""
A Python tuple is an immutable, ordered collection of elements. Immutable
means that once a tuple is created, its elements cannot be changed or
modified. Tuples are similar to lists, but they are enclosed in parentheses ()
instead of square brackets [].

"""

# Creating an empty tuple
empty_tuple = ()
# Creating a tuple with elements
my_tuple = (1, 2, 3, 4, 5)
# Creating a tuple with elements of different types
mixed_tuple = (1, "apple", 3.14, True)
# Creating a single-element tuple (note the comma)
single_element_tuple = (42,)
# You can also create a tuple without parentheses (not recommended for readability)
another_tuple = 1, 2, 3

my_tuple = (1, 2, 3, 4, 5)
# Get the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)

my_tuple = (3, 7, 1, 9, 2, 6)
# Find the maximum element in the tuple
maximum = max(my_tuple)
print("Maximum element:", maximum)
# Find the minimum element in the tuple
minimum = min(my_tuple)
print("Minimum element:", minimum)


# Python Dictionary

"""
A Python dictionary is an unordered collection of key-value pairs. Each key
in a dictionary is unique and immutable, and it maps to a corresponding
value. You can think of a dictionary like a real-world dictionary, where each
word (key) has a definition (value).
You can create a dictionary in Python using curly braces {} and specifying
key-value pairs separated by colons :

"""

# Creating an empty dictionary
empty_dict = {}
# Creating a dictionary with key-value pairs
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Creating a dictionary using the dict() constructor
another_dict = dict(name='Alice', age=25, city='Los Angeles')

# Access

#  Using square brackets []:
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing values using keys
name = my_dict['name']
age = my_dict['age']
city = my_dict['city']
print("Name:", name)
print("Age:", age)
print("City:", city)

#  Using the get() method:
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing values using get() method
name = my_dict.get('name')
age = my_dict.get('age')
city = my_dict.get('city')
print("Name:", name)
print("Age:", age)
print("City:", city)