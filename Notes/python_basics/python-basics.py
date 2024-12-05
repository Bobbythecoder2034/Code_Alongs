"""WHAT IS PYTHON
Python is a high-level, general-purpose, and very popular programming language. Python programming language (latest Python 3) is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry.

Python language is being used by almost all tech-giant companies like - Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.

The biggest strength of Python is huge collection of standard library which can be used for the following:

Machine Learning
GUI Applications (like Kivy, Tkinter, PyQt etc. )
Web frameworks like Django (used by YouTube, Instagram, Dropbox)
Image processing (like OpenCV, Pillow)
Web scraping (like Scrapy, BeautifulSoup, Selenium)
Test frameworks
Multimedia
Scientific computing
Text processing and many more..

Python is currently the most widely used multi-purpose, high-level programming language, which allows programming in Object-Oriented and Procedural paradigms. Python programs generally are smaller than other programming languages like Java. Programmers have to type relatively less and the indentation requirement of the language, makes them readable all the time.
'''
'''PYTHON COMMENTS and Rules for all of programming
Rule 1: Comments should not duplicate the code.
Rule 2: Good comments do not excuse unclear code.
Rule 3: If you can't write a clear comment, there may be a problem with the code.
Rule 4: Comments should dispel confusion, not cause it.
Rule 5: Explain unidiomatic code in comments.
Rule 6: Provide links to the original source of copied code.
Rule 7: Include links to external references where they will be most helpful.
Rule 8: Add comments when fixing bugs.
Rule 9: Use comments to mark incomplete implementations.

# is a single line comment
Anything between """""" is a single to multiple line comment


VARIABLES: Variables do not need to be declared with any particular type, and can even change type after they have been set. Just start with a initial value or not

VARIABLE NAMES: A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
***A variable name must start with a letter or the underscore character
***A variable name cannot start with a number
***A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
***Variable names are case-sensitive (age, Age and AGE are three different variables)
***A variable name cannot be any of the Python keywords.
MULTI VARIABLE CREATION:
#f_name,l_name,age = "Khadeem","Bernard", 21
print(f_name,l_name,age) or print(f_name+l_name+age)

or
#initialValue = start = i = 0

CASTING VARIABLES:If you want to specify the data type of a variable, this can be done with casting.
'''
'''PYTHON DATATYPES:
Python has the following data types built-in by default, in these categories:

Text Type:  str
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Mapping Type:   dict
Set Types:  set, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
None Type:  NoneType
'''

'''Python Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.''' 
""" 

""" Python String Manipulation
String Slicing: returns a piece of a string that is dictated by the inputs:

"""
# test = "This is a test string in Python"
# print(test[5]) # gow to access a character in a string
# print (test[15:35]) # how to access a range of characters in a string


'''String Methods'''
# print(test.upper())#uppercase letters
# spacey = " This has a lot of spacey before and after "
# print(spacey.strip().upper()) #Removes extra spaces
# location = spacey.find('before')
# print(spacey[location:(location*6)]) # like the test[15:35], it finds before and continues to the index value of location * 6
#print(spacey[location:location]) #

'''String Concatenation'''
# print(test + " " + spacey)

# name = 'Take 5'
# amount = 10
# cost = 20
# statements = "I had my favorite candy {2}, I bought a total of {1} for ${0}"
# print(statements.format(cost,amount,name))
# You can finish statement quotes with using the escape { character

"""Conditionals for Python"""

import math #Do not make a comment
"""
x = 23
last_name = "Smiley"
first_name = "KAden"
age = 16
fake_age = "21"
patience = 12
verbal_abuse = 45
tech_is_alive = False
if(tech_is_alive and age > 16) or tech_is_alive == False:
    print("This is what you are doing this is what I want you to do")
if last_name == "Smiley" or last_name == "Kaden":
    print("you arr lucky pirates")
if last_name == "Smiley" and first_name == "Kaden":
    print("Its over for you")
if age > 14:
    print("You are old")
    age += 1
elif age == 19:
    print("Your bday last year was cool")
else:
    print("Generation of Social Goblins")
if first_name == "Kaden":
    print("NO")
if not tech_is_alive:
    print("WHY!!!!!")
print("Kaden Smiley")
print(2**6) 2 to the sixth
print(2**(1/2)) #square root
print(math.sqrt(age)) square root
print(math.pow(2,6))  2 to the power of 6
print(math.radians(30))  converts from decimal to radians
print(math.sin(120))
print(math.tan(90))
print(math.cos(60))
print(math.floor(13.4)) Rounds down
# print(math.gcd(21,14))  finds the greatest common divider


# grade = 84
# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")
# """
# #Lists in python
# """Lists are used to store multiple items in a single variable. It is very similar to arrays."""

# food = ["tacos","Krave","chocolate","Ice Cream","Apple Juice","Steak"]
# print(food)
# print(len(food))  length of the list
# print(food[2])  prints the third item since lists start their index on zero
# print(sorted(food))  This does not change the list itself, it just sorts it.
# # It sorts it by ASCII values of the first character.
# print(food)
# food.sort() This sorts and alters the original list
# print(food)
# food.reverse()  Reverses the order of the list
# print(food)
# food.append("Turkey") Adds to the end of the list.
# # OR
# food[6] = "Turkey" Replaces the item at that index
# print(food)
# print(food.index("Krave"))# returns the index of the item in the list
# del food[4]  deletes the 4th index from the list
# print(food)


# #Dictionaries - key value pairs like a dictionary and definition
# favGames = {"Michael":"Minecraft", "Marissa": "Lockdown Protocol", "Micah": "Lethal Company"}  # The names are the indexs (or keys) and the value is the information associated with that key. Each Username has values with it, like stats or information. Each key can only have one object, but each object can have much more information.
# print(favGames)
# print(favGames.keys())  all the keys in the dictionary
# print(favGames.values())  all the values in the dictionary
# print(len(favGames))  prints the length of the dictionary

#w3schools.com/python/module_math.asp

# users = {"Tommy": 4573283, "John": 4262341, "AJ": 23}
# user = "BoyBoy"
# password = "theTrain"
# login_username = input("What is your username ")
# login_password = input("What is your password ")
# print(users["Tommy"])

# if login_password == users[login_username]:  This needs loops to work
#     print("Success")
# else:
#     print("Failure")

# LOOPS: For Loops used for sequential loops like a list, dictionary set, or even a string
# for thing in food:
#     print(thing)
#  Thing is a temporary nickname for every item in the food list, dictionary, or whatever. First loop, it will find the first item in food and make thing equal to that item and then print thing, showing that item as its value.
# for x in favGames:
#     print(x)
# for thing in food:
#     print("I am the king")
# for x in "Hello":
#     print(x)
# y=2
# for x in "four":
#     y**2
#     print(y)
# While Loops

# index = 2
# while index <= 10:
#     print(index)
#     index += 2

#Functions

'''A function is a block of code which only runs when it is called. you can pass data known as parameters into a function. A function can return data as a result but it is not mandatory'''
contacts = []
# def stands for define
def pretty_print(name, direction):
    print("-----**" + name + "**-----")
    contacts.append(name)
    if(direction[0].upper() == 'N'):
        return "Have fun with the snow"
    elif(direction[0].upper() == "S"):
        print("The Hot South needs fans")
    elif(direction[0].upper() == 'E'):
        print("Has the best pizza")
    else: print("Either from the west or somewhere else. Either way you suck")

pretty_print("Kaden", "wast")

print(contacts)