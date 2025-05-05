#!/usr/bin/python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
x = int(num1)*int(num2)

print(num1,"x",num2,"=",x)
if x > 0:
    print("The result is positive.")
elif x < 0:
    print("The result is negative.")
elif x == 0:
    print("The result is positive and negative.")
