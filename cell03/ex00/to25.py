#!/usr/bin/python3
num1 = int(input("Enter a number less than 25 : \n"))

if num1 > 25:
    print("Error")
else:
    while num1 <= 25:
        print(f"Inside the loop, my variable is {num1}")
        num1 += 1

