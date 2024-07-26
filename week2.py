"""
In Python, arithmetic operators are used to perform mathematical
operations. Here's a list of arithmetic operators in Python:
1    Addition: +
2    Subtraction: -
3    Multiplication: *
4    Division: /
5    Floor Division (integer division): //
6    Modulus (remainder): %
7    Exponentiation: **

"""

# Addition (+):
a = 5
b = 3
result = a + b
print("Addition:", result)  # Output: Addition: 8

# Subtraction (-):
a = 7
b = 4
result = a - b
print("Subtraction:", result)  # Output: Subtraction: 3

# Multiplication (*):
a = 6
b = 5
result = a * b
print("Multiplication:", result)  # Output: Multiplication: 30

# Division (/):
a = 10
b = 3
result = a / b
print("Division:", result)  # Output: Division: 3.3333333333333335

# Floor Division (//):
a = 10
b = 3
result = a // b
print("Floor Division:", result)  # Output: Floor Division: 3

# Modulus (%):
a = 10
b = 3
result = a % b
print("Modulus:", result)  # Output: Modulus: 1

# Exponentiation ():**
a = 2
b = 3
result = a ** b
print("Exponentiation:", result)  # Output: Exponentiation: 8

"""
Python Bitwise Operators
    Introduction
    In Python, bitwise operators are used to perform bitwise operations on
    integers. Here's a list of bitwise operators in Python:
        Bitwise AND (&): Performs a bitwise AND operation on the
    corresponding bits of two integers.

        Bitwise OR (|): Performs a bitwise OR operation on the
    corresponding bits of two integers.

        Bitwise XOR (^): Performs a bitwise XOR (exclusive OR)
    operation on the corresponding bits of two integers.

        Bitwise NOT (~): Performs a bitwise NOT (complement)
    operation, which inverts all the bits of an integer.

        Left Shift (<<): Shifts the bits of an integer to the left by a
    specified number of positions, filling the shifted positions
    with zeros.

        Right Shift (>>): Shifts the bits of an integer to the right by a
    specified number of positions, filling the shifted positions
    with zeros or the sign bit (for signed integers).

"""

# Bitwise AND (&):
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a & b
print("Bitwise AND:", result)  # Output: 1 (0001 in binary)

# Bitwise OR (|):
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a | b
print("Bitwise OR:", result)  # Output: 7 (0111 in binary)

# Bitwise XOR (^):
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a ^ b
print("Bitwise XOR:", result)  # Output: 6 (0110 in binary)

# Bitwise NOT (~):
a = 5  # 0101 in binary
result = ~a
print("Bitwise NOT:", result)  # Output: -6 (1010 in binary for 32-bit integers)

# Left Shift (<<):
a = 5  # 0101 in binary
result = a << 2
print("Left Shift:", result)  # Output: 20 (10100 in binary)

# Right Shift (>>):
a = 10  # 1010 in binary
result = a >> 1
print("Right Shift:", result)  # Output: 5 (0101 in binary)

"""
Python Comparison Operators

Introduction
In Python, comparison operators are used to compare values and return
Boolean results (True or False) based on the comparison. Here's a list of
comparison operators in Python:
    Equal to (==): Returns True if the operands are equal.
    Not equal to (!=): Returns True if the operands are not
equal.
    Greater than (>): Returns True if the left operand is greater
than the right operand.
    Less than (<): Returns True if the left operand is less than
the right operand.
    Greater than or equal to (>=): Returns True if the left
operand is greater than or equal to the right operand.
    Less than or equal to (<=): Returns True if the left operand
is less than or equal to the right operand.

These operators are commonly used in conditional statements, loops, and
other contexts where comparison of values is needed.

"""

# Equal to (==):
a = 5
b = 5
result = a == b
print("Is", a, "equal to", b, "?", result)  # Output: Is 5 equal to 5 ? True

# Not equal to (!=):
a = 5
b = 6
result = a != b
print("Is", a, "not equal to", b, "?", result)  # Output: Is 5 not equal to 6 ? True

# Greater than (>):
a = 6
b = 5
result = a > b
print("Is", a, "greater than", b, "?", result)  # Output: Is 6 greater than 5 ? True

# Less than (<):
a = 5
b = 6
result = a < b
print("Is", a, "less than", b, "?", result)  # Output: Is 5 less than 6 ? True

# Greater than or equal to (>=):
a = 6
b = 6
result = a >= b
print("Is", a, "greater than or equal to", b, "?", result)  # Output: Is 6 greater than or equal to 6 ? True

# Less than or equal to (<=):
a = 5
b = 6
result = a <= b
print("Is", a, "less than or equal to", b, "?", result)  # Output: Is 5 less than or equal to 6 ? True


"""
Python Logical Operators
Introduction
In Python, logical operators are used to combine multiple conditions and
produce a single Boolean result (True or False). Here's a list of logical
operators in Python:
    Logical AND (and): Returns True if both operands are True.
    Logical OR (or): Returns True if at least one of the operands is True.
    Logical NOT (not): Returns True if the operand is False, and False if the operand is True.

"""

# Logical AND (and):
a = True
b = False
result = a and b
print("Logical AND:", result)  # Output: Logical AND: False

# Logical OR (or):
a = True
b = False
result = a or b
print("Logical OR:", result)  # Output: Logical OR: True

# Logical NOT (not):
a = True
result = not a
print("Logical NOT:", result)  # Output: Logical NOT: False


"""
Python Ternary Operators
    Introduction
        The ternary operator in Python is a conditional expression that evaluates a
        condition and returns one of two values depending on whether the condition
        is true or false. It is also known as the conditional expression. The syntax of
        the ternary operator in Python is as follows:
            x = <value_if_true> if <condition> else <value_if_false>
Here's how the ternary operator works:
    <condition> is evaluated first. If it is true, <value_if_true> is
    returned; otherwise, <value_if_false> is returned.
    The ternary operator is an expression, not a statement, so it can
    be used within larger expressions or assignments.

"""

x = 10
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)  # Output: Maximum value: 20

num = 15
result = "Even" if num % 2 == 0 else "Odd"
print(num, "is", result)  # Output: 15 is Odd


"""

Control Statements
    Python if:
            In Python, the if statement is a control flow statement that allows you to
            execute a block of code based on whether a specified condition evaluates to
            True. It is used for decision-making in programming.

"""

"""
Basic if statement:-

    if condition:
        # Code block to execute if the condition is True
        statement1
        statement2
        ...

if-else statement:-
    
    if condition:
        # Code block to execute if the condition is True
        statement1
        statement2
        ...
    else:
        # Code block to execute if the condition is False
        statement3
        statement4
        ...

Chained if-elif-else statement:-
    if condition1:
        # Code block to execute if condition1 is True
        statement1
        statement2
        ...
    elif condition2:
        # Code block to execute if condition2 is True
        statement3
        statement4
        ...
    elif condition3:
        # Code block to execute if condition3 is True
        statement5
        statement6
        ...
    else:
        # Code block to execute if all conditions are False
        statement7
        statement8
        ...

Nested if statement:-
    if condition1:
        if condition2:
            # Code block to execute if both condition1 and condition2 are True
            statement1
            statement2

"""

# Example 1 : EVEN/ODD

number = 7

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


# Example 2 : Largest/Smallest

# Read in three integers from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))
# Assume the first number is both the largest and smallest initially
largest = num1
smallest = num1

# Determine the largest integer
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
# Determine the smallest integer
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
# Print the largest and smallest integers
print("Largest integer:", largest)
print("Smallest integer:", smallest)



# Example 3 : Positive/Negative

num = int(input("Enter an integer: "))
# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")