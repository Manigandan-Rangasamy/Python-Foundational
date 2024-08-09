# Python while

"""
Syntax : 

while <condition>:
    Code block to be executed repeatedly
    as long as the condition is True


# condition is an expression that is evaluated before each
iteration of the loop. If the condition evaluates to True, the
loop body is executed. If the condition evaluates to False, the
loop terminates.

# The colon (:) at the end of the while statement indicates the
start of the indented block of code that will be executed
repeatedly as long as the condition is True.
The code inside the loop block is indented to signify that it
belongs to the loop body.

# The loop continues to execute the code block repeatedly until
the condition becomes False. If the condition never becomes
False, you can end up with an infinite loop.

"""

# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1

# remember to increment i, or else the loop will continue forever.

# The break Statement:
# With the break statement we can stop the loop even if the while condition is true:

"""
using break :
while condition:
    Code block to be executed repeatedly
    as long as the condition is True
    if some_condition:
        break  # Exit the loop if some condition is met
"""

i = 1
while i < 6:
  print(i)
  if i == 3:
    break #breaking the loop when i is equal to 3
  i += 1

# When the break statement is encountered, it immediately exits the while loop, regardless of whether the loop's condition is still True.

# The continue Statement :
# You can use the continue statement to skip the current iteration of a while loop and proceed to the next iteration. 

"""
while condition:
    # Code block to be executed repeatedly
    # as long as the condition is True
    if some_condition:
        continue  # Skip the rest of the loop's code and start the next iteration
        # Code here will be skipped if some_condition is True

"""

# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



#  Python for loop

"""
In Python, a for loop is used to iterate over a sequence (such as a list, tuple,
string, or range) or any iterable object. The for loop executes a block of
code multiple times, once for each item in the sequence or iterable.

syntax : 

for item in sequence:
    Code block to be executed for each item in the sequence


# item is a variable that takes on the value of each item in the
sequence during each iteration of the loop.

# sequence is the sequence of elements over which the loop
iterates. It can be any iterable object, such as a list, tuple,
string, or range.

# The colon (:) at the end of the for statement indicates the start
of the indented block of code that will be executed for each
item in the sequence.

# The code inside the loop block is indented to signify that it
belongs to the loop body.

# During each iteration of the loop, the item variable takes on
the value of the next element in the sequence, and the code
block inside the loop is executed with that value.

"""

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
for x in "banana":
  print(x)

# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break #Exit the loop when x is "banana":
  

# With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
  
for x in range(6):
  print(x)

#   Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# Using the start parameter:

for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# Using break in nested loops:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)
        if element == 5:
            break



# LIST Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

"""
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
# Syntax :

# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Using if else in comprehension:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

# with no if 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

# with range
newlist = [x for x in range(10) if x % 2 == 0]
print(newlist)


# Set in Python

"""
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# *Note: The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# *Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# Length
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

# Accessing a set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# To find if the value is in the set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Add an element
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add two sets 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add any iterbale object
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# *The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).


# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# *Note: If the item to remove does not exist, remove() will raise an error but discard() wont raise an error

# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# *Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)