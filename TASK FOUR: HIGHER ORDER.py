#1.	Write a program to find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.
"""
# using nested function

def  mul7(p):
    if p%7==0:
        return p

def div3(u):
    if u%3!=0:
        return u

def func_hi(mul7,div3,x):
    c=[]
    for i in range(x):
        if div3(i) and mul7(i):
            c.append(i)
    print(c)

func_hi(mul7,div3,100)

# using lambda and filter ()

numbers = list(filter(lambda x: x%7==0 and x%3!==0,range(100)))
print(numbers)


# using list comprehension
numbers1= [i for i in range(100) if i%7==0 and i%3!=0 ]

print(numbers1)



# 2. 	Write a program in Python to  multiple the element of list by itself using traditional function and pass the function to map to
# complete the operation.
d=[1,2,3,4,5]
c=[]


def kk(x):
    for i in x:
        c.append(i*i)
    print(c)
kk(d)

#list1 = [ i*i for i in d ]


# using lambda and map
d=[1,2,3,4,5]

def fun_mul(i):
    return i*i

Final_list = list(map(lambda x: fun_mul(x),d ))

print(Final_list )


# using list comprehension
d=[1,2,3,4,5]

pl = [x*x for x in d ]

print(pl)

"""

#3. 	Write a program to Python find out the character in a string which is uppercase using list comprehension.


x=['raHuL Singh']
y= str(x)

list_upper = [ letter for letter in y if letter.isupper()]

print(list_upper)

#4. 	Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']


Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']


d = list(zip(Student,capital))

final = { k:v for k,v in d }

print(final)

#5. 	Learn More about Yield, next and Generators

"""
Generators are iterators, a kind of iterable you can only iterate over once.
Generators do not store all the values in memory, they generate the values on the fly

yield is a keyword that is used like return, except the function will return a generator.


The next() function returns the next item in an iterator
"""
#6. 	Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

d=[]
Input_String = "Consultadd Training"

def str_rev(Input_String):
    lengt= len(Input_String)
    for x in range(lengt-1,-1,-1):
        d.append(x)
        yield Input_String[x]

for char in str_rev(Input_String):

    print(char)

iter= "Consultadd Training"

def reversed_iterator(iter):
    return reversed((iter))

print (list(reversed_iterator(iter)))

#7. 	Write any example on decorators.
"""
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. 
Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

@gfg_decorator
def hello_decorator(): 
    print("Gfg") 
  
"""
#8. 	Learn about What is FRONT END and its Technologies and Tools
#Make sure to mention at least 5 top notch technologies of Frontend.
#Also mentioned the name of companies using those 5 technologies individually


