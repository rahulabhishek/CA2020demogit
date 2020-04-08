"""
1. 	Write a program to reverse a string.
Sample data: “1234abcd”
Expected Output: “dcba4321”
"""

x = '1234abcd'
print("\""+(x[::-1])+"\"")


"""
2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12

"""
def count_ul():
    x = input("enter the string: ")
    count1=0
    count2=0
    for i in x:
        if (i.islower()):
            count1=count1+1
        elif (i.isupper()):
            count2 = count2 + 1
    print("No. of Lower case Characters :" + str(count1))
    print("No. of Upper case characters :" + str(count2))

count_ul()


#3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_elements(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    print(y)

unique_elements([1,2,3,4,4,4,4,4,4,4])


#4.Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

def func_sort_words(x):
    y=x.split('-')
    y.sort()
    print("\""+"-".join(y)+"\"")

func_sort_words("rahul-aingh")


"""
5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Sample input:
Hello world
Practice makes perfect

Expected Output:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

v= input(" user input: ")
b = v.upper()
print(b)


#6. Define a function that can receive two integral numbers in string form and compute their sum and print it in console.



def func_sum(x,y):
    sum=int(x)+int(y)
    print(sum)
func_sum("2","3")

or.....

def func_sum(x,y):
    sum=(x)+(y)
    print(sum)
func_sum("2","3")

"""
7. Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.
"""


def length_of_string(str1, str2):
    if len(str1)> len(str2):
        print(str1)
    elif len(str1)< len(str2):
        print(str2)
    else:
        print(str1 + "\n" + str2)

length_of_string("rahull","singh")



#8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def func_tup(x,y):
    z=[]
    for i in range(x,y):
        z.append(i**2)
    print(tuple(z))

func_tup(2,20)

"""
9. Write a function called showNumbers that takes a parameter called limit.
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
Example: If the limit is 3 , it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD
"""

def showNumbers(limit):
    for i in range(0,limit):
        if i%2==0:
            print(str(i)+ " even")
        else:
            print(str(i)+ " odd")

showNumbers(5)


# 10.Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)


def find_even(x,y):
    s=[]
    for i in range(x,y):
        s.append(i)
    p = list(filter((lambda x:x%2==0),s))
    print(p)

find_even(1,21)

"""
11.Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
Hints: Use map() to generate a list.
Use filter() to filter elements of a list
Use lambda to define anonymous functions
"""
def fun_map_filter(d):
    l = list(filter(lambda x:x%2==0,d))
    j= list(map(lambda x:x*x,l))
    print(j)


fun_map_filter([1,2,3,4,5,6,7,8,9,10])

#12.Write a function to compute 5/0 and use try/except to catch the exceptions

def fun_try_catch(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("ZeroDivisionError: division by zero  exception occurred")
    finally:
        print("The 'try except' is finished")

fun_try_catch(5,0)



#13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce Goal : Turn [1,2,3,4,5,6,7] to 1234567


from functools import reduce
given_list = [[1,2,3],[4,5,6],[7,8,9]] #List to be flattened
flat_list = reduce(lambda z,y:z + y, given_list)
print("Original List:",given_list)
print("Flattened List:",flat_list)

#14.What is the output of the following codes:
#(i)
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#solution: 2

#(ii)
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()


#solution: NameError: name 'f' is not defined


