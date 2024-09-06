school = "west-mec"

#Snake Case example
first_name = "Kaden"
last_name = "Smiley"

print(first_name)
print(last_name)
print(school)
print(type(school))
print(type (first_name))

message = """
food
and games
are cool"""
print(message)

age = 16
alive = True
fav_foods = ['mexican', "italian", 'chinese']
print(first_name + " " + str(age) + " " + str(alive) + " " + str(fav_foods))
meat = True
dairy = "better"
samsung = 578
print(str(meat)+" "+dairy+" "+str(samsung))
print(str(84))
print(str(True))
print(type(str(True)))
print(int(True) + int(False) + float("55.5"))
print(bool(1))

age_1 = 23
age_2 = 56
if age_2 > 45:
    print("They OLD")
if age_2 == age_1:
    print("Mission Failed")
if age_1 != age_2:
    print("Success")
if age_1 <= age_1 + age_2:
    print("Math")
best_friend = "Zach"
thinks_bf = "Tuesday"
if best_friend != thinks_bf:
    print("Good Jorb")
if("25" == str(25)):
   print("You have to convert before hand for Python, because it doesn't auto convert")

alive = False
year = 2024
time = 4.7

if alive == True & year == 2024:
    print("YIPPEEE")
if alive:
    if year == 2024:
        print("Better")
    print("Me")
else:
    print("They have failed you")
money = 39
if money <= 20:
    print("Broke Netflix")
elif money >= 21 & money <= 60:
    print("Movie theatre")
elif money >= 61 & money <= 80:
    print("Dinner")
else:
    print("Sky Diving")

"""User Interactions"""
"""first_name = input("What is your first name?")
print("Good Morning " + input("What is your name? "))"""
"""This works, It is in comments to make the rest of the code run automatically"""
"""
time = input("How many hours did the ride take? ")
speed = input("What was the speed? ")
distance = int(time) * int(speed)

print(("The speed was " + str(speed) + "mph and the time was " + str(time) + " hours. The total distance was " + str(distance) + " miles."))

speed = float(input("How fast in MPH?"))
easy way to convert inputs directly into numbers, in this case, float means it can take decimals.
"""
"""
CALCULATING THE HYPOTENUSE OF A TRIANGLE WITH THE PYTHAGOREAN THEOREM

side_A = float(input("What is the length of side A: "))
side_B = float(input("What is the length of side B: "))
side_A *= side_A
side_B *= side_B
side_C = side_A+side_B
side_C = side_C ** float(1/2)
print("The hypotenuse of the triangle is " + str(side_C) + "cm")

"""

#Functions

x = 14
y = 25

def add_function(num1,num2):
    print(str(num1+num2))

add_function(x,y)

my_name_is = "Kaden"
def name_function(myname):
    print(str(myname) + " is the favorite child.")

name_function(my_name_is)