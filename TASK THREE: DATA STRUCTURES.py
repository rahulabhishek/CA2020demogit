# 1 Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
"""
x= [1,2,3,4,"rahul","mohan",7.9,8.9,9.9,9+1j]
count=0
for i in x:
   print(i)
   count=count+1
print(count)

#2.    Create a list of size 5 and execute the slicing structure


x= [1,2,3,4,"rahul"]

print(x[1:5])
print(x[0:4])
print(x[0:5:2])



#3 Write a program to get the sum and multiply of all the items in a given list.
'''
x= [1,2,3,4,5]

print(sum(x))
y= 1
for i in x:
   y=i*y
print(y)


# 4 Find the largest and smallest number from a given list.

x= [1,2,3,4,5]

print(max(x))
print(min(x))



#5.    Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

x= [1,2,3,4,5,6,11,28,32,34,44,45]
y=[]
for i in x:
   if i%2!=0:
       (y.append(i))
print(y)


#6.    Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

x= [1,2,3,4,5,6,7,8,9,10]



x= []
for i in range(1,31):
   x.append(i*i)

print(x[:5])
print(x[-5:])
'''
7. Write a program to replace the last element in a list with another list.
Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
Expected output: [1,3,5,7,9,2,4,6,8]

x= [1,3,5,7,9,10]
y= [2,4,6,8]
x.remove(10)
x.extend(y)
print(x)




8. Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
Expected Result: {1:10,2:20,3:30,4:40}


a={1:10,2:20}
b={3:30,4:40}
a.update(b)

print(a)



9. Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
Sample data (n=5)
Expected Output: {1:1,2:4,3:9,4:16,5:25}


y={}

for x in range(1,6):
   y.update({x:x*x})
print(y)

10.    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
34,67,55,33,12,98
The output should be:
[‘34’,’67’,’55’,’33’,’12’,’98’]
(‘34’,’67’,’55’,’33’,’12’,’98’)



user_input = input("enter the no: ")

xlist = user_input.split(",")

xtuple = tuple(xlist )


print(xlist)
print(xtuple)

"""













