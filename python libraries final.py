#!/usr/bin/env python
# coding: utf-8

# ### Instructions
# 
# * Sign up for the free course on Educative, __Learn Python 3 From Scratch__
# * https://www.educative.io/courses/learn-python-3-from-scratch
# * Complete the programming exercises below as you go through the course.
# * Delete or comment out the line of code in each cell which says `raise NotImplementedError()` and replace it with your own.

# # Educative - Libraries
# 
# https://www.educative.io/courses/learn-python-3-from-scratch/RLQYXWpMZvO

# ### Exercises

# Write code in the cell below.
# * Import the datetime module.
# * Create a variable called `date_today` and assign it the current date.
# * Print `date_today`
# * Create a variable called `time_today` and assign it the current time with the format `%H:%M:%S`.
# * Print `time_today`

# In[8]:


# Importing modules at the beginning of the program is a good practice

# YOUR CODE HERE
import datetime
date_today = datetime.date.today()
print(date_today)
time_today=datetime.datetime.now()
print(time_today.strftime("%H:%M:%S"))


# Write code in the cell below.
# * Import the date class from the datetime module.
# * Using the date class, create a variable called `date_today` and assign it the current date.
# * Print `date_today`

# In[9]:



# YOUR CODE HERE
from datetime import date
date_today = date.today()
print(date_today)


# Write code in the cell below.
# * Import the datetime module and name it `dt`.
# * Create a variable called `date_today` and assign it the current date.
# * Print `date_today`
# * Create a variable called `time_today` and assign it the current time with the format `%H:%M:%S`.
# * Print `time_today`

# In[10]:



# YOUR CODE HERE
import datetime as dt
date_today = dt.date.today()
print(date_today)
time_today = dt.datetime.now()
print(time_today.strftime("%H:%M:%S"))


# Google the term `python standard library` to find the latest documentation on the Python Standard Library. Provide a short description of the purpose of some of the common modules listed below. (The short description on the main documentation page for the Python Standard Library is sufficient. I'm only trying to introduce you to the standard library and where you can find additional information on particular modules. You don't need to do any further reading for now.)
# 
# * csv -
# * datetime -
# * math -
# * os -
# * re -
# * string -
# * unittest -

# csv -csv file reading and writing
# datetime -basic date and time types
# math -mathematical functions
# os -miscellaneous operating system interfaces
# re - regular expression operations
# string -common string operations
# unittest - unit testing framework

# Answer in the cell below.
# 
# What is PyPI?

# The python packaging index, it is a type of repository
