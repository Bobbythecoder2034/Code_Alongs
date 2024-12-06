users = input("Enter a String: ")
small = users.lower()
big = users.upper()
backwards = users[::-1]
count = 0
replaced = users.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')

for things in users:
    count = count + 1


print("Uppercase: " + big)
print("Lowercase: " + small)
print("Reversed: " + backwards)
print("Replaced: " + replaced)
print("Characters: " + str(count))

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("Addition: " + str((x+y)))
print("Subtraction: " + str((x-y)))
print("Multiplication: " + str((x*y)))
print("Division: " + str((x/y)))
print("Modulus: " + str((x%y)))
print("Exponentation: " + str((x**y)))




first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello there " + first_name + " " + last_name)
full_name = first_name + " " + last_name
number = input("Enter your favorite number: ")
modified_name = full_name + number
print("Your modified name is " + modified_name)







def greet_user(name):
    response = "Hello there " + name
    return response

def convert_to_celcius(fahrenheit):
    temp = (fahrenheit - 32) * (5/9)
    return temp

def calculate_area(length, width):
    return "Area of the rectangle: " + str(length*width)

print(greet_user("Anne"))
print("Temperature in Celcius: " + str(convert_to_celcius(45)))
print(str(calculate_area(5,4)))