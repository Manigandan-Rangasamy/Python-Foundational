"""
Python Functions:


A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

function is defined using the "def" keyword:

"""
def my_function():
  print("Hello from a function")

# To call a function, use the function name followed by parenthesis
my_function()

"""
Arguments/Parameters:

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.

By default, a function must be called with the correct number of arguments. 
If your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# *Arguments are often referred as args in Python documentations.
"""

def my_function(fname):
  print(fname + " Hanks")

my_function("Tom")
my_function("Robb")
my_function("Ron")

# Function with 2 arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

"""
Keyword Arguments:
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

"""

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Robb", child2 = "Tom", child3 = "Ron")

"""
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value

"""
def my_function(country = "India"):
  print("I am from " + country)

my_function("Sweden")
my_function("UK")
my_function()
my_function("Brazil")

# Passing list as an argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

"""
Return Values
To let a function return a value, use the return statement
you can return values from a function using the return statement.
# *The return statement is used to exit the function
"""

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

"""
The pass Statement
function definitions cannot be empty.
If you want function definition with no content, put in the pass statement to avoid getting an error.

"""
def myfunction():
  pass

"""
Scope:
A variable is only available from inside the region it is created. This is called scope.

Local Scope:
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# *Global variables are available from within any scope, global and local.
"""

# local scope

def myfunc():
  x = 300
  print(x)

myfunc()

"""
Function Inside Function
The variable decalared inside a function is not available outside the function, 
but it is available for any function inside the function:

"""

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# *GLOBAL 
# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

"""
Naming Variables
If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables, 
one available in the global scope (outside the function) and one available in the local scope (inside the function)
"""

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

"""
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

"""

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# * use the global keyword if you want to make a change to a global variable inside a function.

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)