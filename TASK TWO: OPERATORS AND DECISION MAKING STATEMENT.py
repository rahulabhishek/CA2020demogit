# 1.
user_input = int(input("Enter the number: "))

if (user_input % 3 == 0 and user_input % 5 == 0):
    print("Consultadd Python Training")
elif (user_input % 3 == 0):
    print("Consultadd")
elif (user_input % 5 == 0):
    print("c")
else:
    print("no out of scope")

# 2.
while True:
    user_input = int(input("choose the Arithematic Operation from 1-5: "))
    if (user_input <= 5 and user_input > 0):
        break
    else:
        print("Enter options in digits between 1 and 5")

if (user_input == 1):
    first = int(input("Enter the first number: "))
    second = int(input("Enter the Second number: "))
    Addition = (first + second)
    if (Addition < 0):
        print("zsa")
    else:
        print("Addition : " + str(Addition))

elif (user_input == 2):
    first = int(input("Enter the first number: "))
    second = int(input("Enter the Second number: "))
    Substraction = (first - second)
    if (Substraction < 0):
        print("zsa")
    else:
        print("Substraction: " + str(Substraction))

elif (user_input == 3):
    first = int(input("Enter the first number: "))
    second = int(input("Enter the Second number: "))
    Division = (first / second)
    if (Division < 0):
        print("zsa")
    else:
        print("Division : " + str(Division))

elif (user_input == 4):
    first = int(input("Enter the first number: "))
    second = int(input("Enter the Second number: "))
    Multiplication = first * second
    if (Multiplication < 0):
        print("zsa")
    else:
        print("Multiplication: " + str(Multiplication))

elif (user_input == 5):
    first = int(input("Enter the first number: "))
    second = int(input("Enter the Second number: "))
    first1 = int(input("Enter the first number: "))
    second2 = int(input("Enter the Second number: "))
    Average = (first + second + first1 + second2) / 4
    if (Average < 0):
        print("zsa")
    else:
        print("Average: " + str(Average))


# 3.
def flow_chart(a, b, c):
    avg = (a + b + c) / 3
    print("avg: " + str(avg))

    if (avg > a and avg > b and avg > c):
        print("avg is higher than a,b,c")
    elif (avg > a and avg > b):
        print("avg is higher than a,b")
    elif (avg > a and avg > c):
        print("avg is higher than a,c")
    elif (avg > b and avg > c):
        print("avg is higher than b,c")
    elif (avg > a):
        print("avg is just higher than a")
    elif (avg > b):
        print("avg is just higher than b")
    elif (avg > c):
        print("avg is just higher than c")


# 4.
while True:
    User_input1 = int(input("Enter the first number : "))
    if User_input1 < 0:
        break
    elif User_input1 > 0:
        print("Good Going")
    else:
        print("Zero is neither positive nor negative, please enter a number either greater or less than 0")

    print("It’s Over")


# 5.
def numfinder():
    for x in range(2000, 3200):
        if (x % 7 == 0 and x % 5 != 0):
            print(x)


# 6.
"""
Traceback (most recent call last):
File "/Users/rahul/PycharmProjects/practice/dsgs.py", line 6, in <module>
    for i in x:
TypeError: 'int' object is not iterable
Multiple values must be provided for x so that I can iterate through that.
"""
# 7.
for x in range(0, 6):
    if x == 3 or x == 6:
        continue
        print(x)

# 8.
user_input = input("enter the string: ")


def match_string(user_input):
    nums = 0
    letter = 0
    other = 0
    for x in user_input:
        if x.isalpha():
            letter += 1
        elif x.isdigit():
            nums += 1
        else:
            other += 1
        print("Letters: " + str(letter))
        print("Digits: " + str(nums))


# 9.
luck_number = 5
while True:
    number = int(input("guess the lucky number: "))
    if (number == luck_number):
        print("You Won! ")
        break
    else:
        answer = input("would you like to guess again: Enter yes/no ")
        if (answer.lower() == ('yes')):
            continue
        else:
            print("Bye...you have a good day")
            break

# 10.

lucky_number = 5
counter = 1

while (counter <= 5):
    number = int(input("guess the lucky number: "))
    if (number == lucky_number):
        print("Good guess!")
    elif counter == 5:
        break
    else:
        print("Try again!")

    counter = (counter + 1)

print("Game over!")

# 11.
lucky_number = 5
counter = 1

while (counter <= 5):

    number = int(input("guess the lucky number: "))
    if (number == lucky_number):
        print("Good guess!")
        break
    else:
        print("Try again!")

    counter = (counter + 1)

print("Sorry but that was not very successful")
