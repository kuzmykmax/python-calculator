# name = "Max"
# age = 100
# height= 180
# student=False
# print("name =",name)
# print("age =",age)
# print("height=",height)
# print("student=",student)
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(student))
from tkinter.font import names

# x = int(input("Enter the first number "))
# y = int(input("Enter the second number "))
# print("sum =",x+y)
# print("difference =",x-y)
# print("product =",x*y)
# print("quotient =",x/y)
# print("modulus =",x%y)

# age=int(input("Enter your age "))
# if age>18:
#     print(True)
# else:
#     print(False)
# if age<65:
#     print(True)
# else:
#     print(False)
# if 18<age<65:
#     print(True)
# else:
#     print(False)
# word=input("Enter the word ")
# print(word.upper())
# print(word.lower())
# print(len(word))
# print(word[2])
# name = input("Enter your name ")
# age = int(input("Enter your age "))
# print(f"Hello,{name}! You are {age} years old and in 10 years it will be {age+10}")

x= int(input("Enter the first number: "))
y= int(input("Enter the second number: "))
operation=input("Choose the operation: '+' ; '-' ; '*' ; '/' ")
# if operation != "+" or "-" or "*" or "/":
#     print("You enter the wrong operation! ")
if operation == "+":
    print(x + y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    if y==0:
        print("We cannot divide by zero")
    else:
        print(x/y)
else: print("Wrong operation")


