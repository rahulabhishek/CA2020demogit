"""1.	Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

import math
import numpy



def func_fm(x):
    C=50
    H=30
    Q=[ math.sqrt((2*C*D)/H)  for D in x ]
    print(Q)

func_fm([20,30])



2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.



class Shape(object):
    def __init__(self):
       pass

    def func_area(self):
        return 0

class Square (Shape):
    def __init__(self,l):
        self.length = l

    def func_area(self):
        print("Area of the square :"+ str(self.length*self.length))


class Rectangle (Shape):
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def func_area(self):
        print("Area of the rectangle :"+ str(self.length*self.breadth))

x= Square(7)
x.func_area()

y=Rectangle(7,9)
y.func_area()


3.Create a class to find the three elements that sum to zero from a set of n real numbers.
Input array: [-25,-10,-7,-3,2,4,8,10]
Output: [[-10,2,8],[-7,-3,10]]



class ddd(object):

        def __init__(self,x):
            result= []
            for i in range(len(x)):
               if i[0]+i[1]+i[2]==0:
                   print(i)

t= [-25,-10,-7,-3,2,4,8,10]
a= ddd(t)




#4. What is the output of the following code? Explain your answer as well.


class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

#there will be an "AttributeError" error, since Derived_Test object has no attribute 'x' but only 'y'

class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main()


#Output will be (1 2) since  "der" class is using  the super() function to inherit the init function from the A class ( here x = 1 and y=2)



class A:
    def __init__(self,x):
        self.x = x

    def count(self,x):
        self.x = self.x+1

class B(A):

    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y

    def count(self):
        self.y += 1

def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)

main()


# Output will be (3 1) since B class inherits the x value from the class A , but the count function in class B adds a count to y making it 1

class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i;


class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i;


obj = B()

# output will be 30 since the value i(15) is  inherited from a function in Class A and later multiplied with 2.



5.Create a Time class and initialize it with hours and minutes.
Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Make a method displayTime which should print the time.
Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.



class Time():
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    def addTime(time1, time2):
        time3 = Time(0, 0)
        if time1.mins + time2.mins > 60:
            time3.hours = (time1.mins + time2.mins) / 60
        time3.hours = time3.hours + time1.hours + time2.hours
        time3.mins = (time1.mins + time2.mins) - (((time1.mins + time2.mins) / 60) * 60)
        return time3

    def displayTime(self):
        print("Time is: ", round(self.hours), "hours and", round(self.mins), "minutes.")

    def displayMinute(self):
        print("Total mins in time: ",round((self.hours * 60)))



x = Time(2,50)
y = Time(1,20)
z = Time.addTime(x,y)
z.displayTime()
z.displayMinute()

"""





