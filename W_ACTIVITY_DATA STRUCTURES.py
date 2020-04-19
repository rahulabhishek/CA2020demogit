
# 1 Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.

x= [1,2,3,4,"rahul","mohan",7.9,8.9,9.9,9+1j]
count=0
for i in x:
   print(i)
   count=count+1
print(count)

#2.Create a list of size 5 and execute the slicing structure


x= [1,2,3,4,"rahul"]

print(x[1:5])
print(x[0:4])
print(x[0:5:2])

"""

#3.Create a list of given structure and run

Access list [1, 2, 3, 4]
Access list [600,  700]
Access list [100, 300, 500, 600, 800]
Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list [10]
Access list [ ]
"""

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print(x[5][:4])
print(x[6:8])
print(x[:10:2])
print(x[::-1])
print(x[5][5][:1])
print([])




#4 Create a list of thousand number using range and xrange and see the difference between each other.

First of all xrange doesnt exist in python3.
The difference is that range returns a Python list object and xrange returns an xrange object.

#5.How Tuple is beneficial as compare to the list?

Tuples are stored in a single block of memory. Tuples are immutalbe so, It doesn't require extraspace to store new objects.
We can use tuples in a dictionary as a key but it's not possible with lists

#6.Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.

y=[]
for x in range(1,100):
    if x%3 == 0 and x%2==0:
        y.append(x)
print(y)


#7.Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.


x= "rahul"
y=(x[::-1])
print(y)
v=['a','e','i','o','u']
j=[]

for i in y:
    for m in v:
        if i==m:
            #j.append(i)
            print("Index of  " + str(i) + ": " + str(y.index(i)))

#8.Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.

x= "hello my name is abcde"
y = x.split(" ")
print(y)
z=[]
for i in y:
    if len(i)%2==0:
        z.append(i)
print(z)


#9.Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.

x=[1,2,3,4,5,6,7,8,9,-1]
z=[]
for i in x:
    for j in x:
        if (i+j) == 8:
            p = (i,j)
            z.append(p)
print(z)



#10. 
y_even= [2,4,6,8,10]
x_odd= [1,3,5,7,9]

count=0

while count<11:
    user_input= int(input ("enter the number in the range of 1,50: "))
    if (user_input)%2 == 0:
        if (len(y_even)+5) < (len(y_even)+6):
                y_even.append((user_input))
    count=count+1

print(y_even)
print(x_odd)

y_even= [2,4,6,8,10]
count=0
while (len(y_even)+5) < (len(y_even)+6) :
    user_input= int(input ("enter the number in the range of 1,50: "))
    y_even.append((user_input))
    count=count+1

print(y_even)
print(x_odd)


#11. 

x = '12abcbacbaba344ab'
z= list(x)
y=[]
for i in z:
    if i.isalpha():
        y.append(i)
print(y)

print("a: "+ str(y.count('a')))
print("b: "+ str(y.count('b')))
print("c: "+ str(y.count('c')))

#alternate way:

x = '12abcbacbaba344ab'

print("a: " + str(x.count("a")))
print("b: " +str(x.count("b")))
print("c: " + str(x.count("c")))




#12.Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

def func_tup(x):
    y=[]
    for i in x:
        if i%2==0:
            y.append(i)
    print(tuple(y))
x= (1,2,3,4,5,6,7,8,9,10)
func_tup(x)


