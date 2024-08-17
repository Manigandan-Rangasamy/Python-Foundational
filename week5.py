#Recursion

"""
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function.
Using a recursive algorithm, certain problems can be solved quite easily.

Step1 - Define a base case: Identify the simplest case for which the solution is known or trivial. This is the stopping condition for the recursion, as it prevents the function from infinitely calling itself.

Step2 - Define a recursive case: Define the problem in terms of smaller subproblems. Break the problem down into smaller versions of itself, and call the function recursively to solve each subproblem.

Step3 - Ensure the recursion terminates: Make sure that the recursive function eventually reaches the base case, and does not enter an infinite loop.

step4 - Combine the solutions: Combine the solutions of the subproblems to solve the original problem.

"""

# factorial(n) = n * factorial(n-1)
# factorial(1) = 1
# factorial(2) = 2*1
# factorial(5) = 5*4*3*2*1
# factorial(7) = 7*6*5*4*3*2*1

#Without recursion
def factorial(n):
    product = 1
    for i in range(1,n+1):
        product = product * i
    return product

result  = factorial(5)
print(result)

# Using Recursion
def fact(n):
    if (n <= 1):
        return 1
    else:  
        return n*fact(n-1);    


# Modules and Packages

"""
The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file.
It is an executable file and to organize all the modules we have the concept called Package in Python.

The package is a simple directory having collections of modules. This directory contains Python modules.

Example packages : Numpy, Pandas

"""
# 1
import test_module

test_module.hello()
test_module.Bye()

# 2
import test_module as tm

tm.Bye()
tm.hello

# 3
from test_module import hello

hello()

# 4
from test_module import Bye

Bye()

# 5
from test_module import hello as h

h()


#FILE HANDLING

"""
Python supports file handling and allows users to handle files 
i.e., to read and write files, along with many other file handling options, to operate on files.

Python File Open
Before performing any operation on the file like reading or writing, first, we have to open that file. 
For this, we should use Python’s inbuilt function open() 
but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

# f = open(filename, mode)

# modes available
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
a: open an existing file for append operation. It won't override existing data.
r+: To read and write data into the file. This mode does not override the existing data, but you can modify the data starting from the beginning of the file.
w+: To write and read data. It overwrites the previous file if one exists, it will truncate the file to zero length or create a file if it does not exist.
a+: To append and read data from the file. It won't override existing data.

"""

file = open('example.txt', 'r')
for each in file:
    print (each)

file = open('example.txt', 'w')
file.write('hello world !')
file.close()

"""
In Python, with statement is used in exception handling to make the code cleaner and much more readable. 
It simplifies the management of common resources like file streams.
"""
# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')


import os

def create_file(filename):
    with open(filename, 'w') as f:
        f.write('Hello, world!\n')
    print("File " + filename + " created successfully.")

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)


def append_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)
    print("Text appended to file " + filename + " successfully.")

def rename_file(filename, new_filename):
    os.rename(filename, new_filename)
    print("File " + filename + " renamed to " + new_filename + " successfully.")


def delete_file(filename):
    os.remove(filename)
    print("File " + filename + " deleted successfully.")


# NumPy ==> numerical python

"""
NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# https://github.com/numpy/numpy

In Python we have lists that serve the purpose of arrays, but they are slow to process.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.
"""
# installing numpy == >python -m pip install numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))


import numpy as np

# 1D array
a = np.array([1, 2, 3, 4, 5])

# 2-D Arrays
b = np.array([[1, 2, 3], [4, 5, 6]])

# 3-D arrays

c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# Dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)

# Size
print(a.size)
print(b.size)
print(c.size)

# Rows and columns
print(a.shape)
print(b.shape)
print(c.shape)

# dataType

print(a.dtype)
print(b.dtype)
print(c.dtype)

# transpose : rows -- > columns

print(c.transpose())


# PANDAS ==> Data Preparation

"""

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.

Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. 
This is called cleaning the data.

#https://github.com/pandas-dev/pandas
"""

# Pandas Series
"""
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
"""
# Series
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

print(myvar[0])

# Series with indexing

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["y"])


# Key/value objects as series
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories) # The keys of the dictionary become the labels.

print(myvar)


# only with some keys
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


# DATA FRAMES
"""
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

Series is like a column, a DataFrame is the whole table.
"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
#refer to the row index:
print(df.loc[0])
#use a list of indexes:
print(df.loc[[0, 1]])


# Naming your own index in Dataframe
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
#refer to the named index:
print(df.loc["day2"])

# loading files into dataframe -- >Read CSV
import pandas as pd

df = pd.read_csv("data.csv")
print(df) 


# JSON objects as Dataframe
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 

# Analyzing
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

# default 5 rows
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())
print(df.tail()) 
print(df.info()) 