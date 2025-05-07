#!/usr/bin/python3
x = float(input("Give me a number: "))

# if x:
#    print("This number is an integer.")
# elif x.isdecimal():
#    print("This number is a decimal.")

if x.is_integer():
   print("This number is an integer.")
else:
   print("This number is a decimal.")