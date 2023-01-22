# Python FUll Course - Bro Code

# variable - a container for a value.

# strings - series of characters
# first_name = "John"
# last_name = "Armada"
# print("Hello " + first_name + " " + last_name)

# int - a whole number
# age = 18
# print("Your age is: " + str(age))
# print(type(age))

# float = a decimal number
# height = 176.4
# print(type(height))

# boolean - True or False
# human = True
# print("Are you a human? " + str(human))
# print(type(human))


# Multiple assignment - allows us to assign multiple variables at the same time in one line of code
# John = 100
# Job = 100
# Jay = 100

# John = Job = Jay = 100

# print(John)


# String Methods

# name = "John Armada"
# name = "18"
# print(len(name))
# print(name.find("o"))
# print(name.upper())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("o", "a"))
# print(name*3)

# Type casting - convert the data type of a value to another data type
# x = 1  # int
# y = 2.0  # float
# z = "3"  # str

# x = float(x)
# y = float(y)
# z = float(z)

# print(x)
# print(y)
# print(z)


# User input
# name = input("What is your name?: ")
# age = int(input("How old are you? "))
# height = float(input("How tall are you? "))

# print("Hello " + name)
# print("You are " + str(age) + " years old")
# print("You are " + str(height) + "cm tall")


# Math Functions
# import math

# pi = -3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(420))
# print(max(x, y, z))
# print(min(x, y, z))


# String slicing
# slicing - create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# name = "Christ John Armada"

# first_name = name[:11]
# last_name = name[12:]
# funky_name = name[::4]
# reversed_name = name[::-1]

# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"

# slice = slice(7, -4)

# print(website1[slice])
# print(website2[slice])


# If statement - a block of code that will execute if it's condition is true
# == - comparison operator for equality
# = - creating a value

# age = int(input("How old are you?: "))

# if age >= 18:
#     print("You are a century old!")
# elif age == 100:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")


# Logical Operators - (and, or, not) = used to check if two or more conditional statements is true

# temp = int(input("What is the temperature outside?: "))

# if not (temp >= 0 and temp <= 30):
#     print("the temperature is bad today!")
#     print("stay inside!")
# elif not (temp < 0 or temp > 30):
#     print("the temperature is good today!")
#     print("go outside")


# while loop - a statement that will execute its block of code, as long as its condition remains true
# name = None

# while not name:
#     name = input("What is your name? ")

# print("Hello " + name)


# while loop = unlimited
# for loop = limited

import time
# For loop = a statement that will execute its block of code a limited amount of times
# e.g. - timer, countdown

# for num in range(11):
#     print(num)

# for i in range(50, 100 + 1, 2):
#     print(i)\

# for letter in "Christ John Armada":
#     print(letter)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")


# nested loops = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# Continue

# Learning Git
# first create repository and coppy ssh url
# go to git bash, add "git clone {ssh url}"
# You're ready to go

# When adding a new file, enter "git add app.py(e.g)"
# git commit -m "added app.py file (e.g)" - when you want to add a message
# git diff -will tell us everything the difference between the current version in our directory and the version in git

# press q when there is ": "
# git add . - to add multiple files at one time
# git commit - m

# git checkout -b {name} - having a new branch/initial
# git push --set-upstream origin {Brach-A} - after the new, commit this
# git checkout main - go back in default branch

# git status - tell what branch are you on

# I am Christ John
# How are you?
# Are you in college?
