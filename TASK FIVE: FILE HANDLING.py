#1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

def jj(x):
    try:
        print(x/0
    except SyntaxError:
        print("Exception")
    finally:
        print("The 'try except' is finished")


jj(5)

#2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw
# an exception and ask them to enter the name again. Make sure to use read only mode.





#3.Write a program to handle an error if the user entered the number more than four digits it should return
# “Please length is too short/long !!! Please provide only four digits”

while True:
     user_input = input("Enter the number: ")
     try:
          if len(user_input) > 4:
               raise Exception (print("Please length is too short/long !!! Please provide only four digits"))
          elif len(user_input) <= 4:
               print("execution complte")
               break
     except Exception :
          pass
     finally:
          pass
#4. 	Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
#5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept.

#6. 	Read any file using Python File handling concept and return only the even length string from the doc.txt file.
""""
Consider the content as:
	Hello I am a file
	Where you need to return the data string
	Which is of even length
	Make sure you return the content in
	The same link as it is present.
"""

file_open = open('doc','r')
file_string=[]
file_length=[]
for data in file_open:
     file_string.append((data[0:-1]))
     file_length.append(len(data))

final_zip = list(zip(file_string,file_length))
final1 = { k:v  for k,v in final_zip   if (v %2==0)}

print(final1)