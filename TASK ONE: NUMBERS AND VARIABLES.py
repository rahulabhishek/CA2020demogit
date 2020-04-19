# PYTHON ASSIGNMENT -1

# 1.
x, y, z = 1, 'e', 17.8

print(x, y, z)
print('\n')


# 2.
def swap3(x, y):
    y = 1 + 2j
    z = x + y

    l = (z - x)
    c = (z - y).real
    print("Swapped Value for x: " + str(l))
    print("Swapped Value for y: " + str(c) + '\n')


# 3.Swap two numbers using the third variable

def swap1(x, y):
    z = y + x
    x = z - x
    y = z - y
    print("Swapped Value for x: " + str(x))
    print("Swapped Value for y: " + str(y) + '\n')


swap1(5, 6)


# Swap two numbers without using any third variable

def swap2(x, y):
    x = x + y
    y = x - y
    x = x - y
    print("Swapped Value for x: " + str(x))
    print("Swapped Value for y: " + str(y))


swap2(5, 6)

# 4 Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

# Python 3.x Version

User_input = input("Enter the value to be printed : ")
print("User Entered Value: " + User_input)

# Python 2.x
User_input = raw_input("Enter the value to be printed : ")
print("User Entered Value: " + User_input)

# 5.
while True:
    User_input1 = int(input("Enter the first number : "))
    if User_input1 <= 10:
        break
    else:
        print("Enter any number in between 1-10")

while True:
    User_input2 = int(input("Enter the Second number : "))
    if User_input2 <= 10:
        break
    else:
        print("Enter any number in between 1-10")

z = User_input1 + User_input2
result = z + 30
print("User Entered Value: " + str(result))


# 6.
def check_data_type(data):
    if type(data) == int:
        print("The input value data type is: int")
    elif type(data) == str:
        print("The input value data type is: string")
    elif type(data) == float:
        print("The input value data type is: float")
    else:
        print("unknown data type")


# 7.
UpperCamal: "firstname"
ladderCase: "middlename"
UPPERCASE: "lastname"

# 8.
a = 1
a = "j"
print(a)

# Yes the value will change since the variable a has been assigned a new value. Python will change the variable type if the variable value is set to another value.
