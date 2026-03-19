x= int(input("Enter the first number: "))
y= int(input("Enter the second number: "))
operation=input("Choose the operation: '+' ; '-' ; '*' ; '/' ")
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


