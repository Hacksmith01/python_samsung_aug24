# Program to check if a number is Perfect Square

import math
number = int(input("enter the number you want to check is a perfect square: "))
sq_root=math.sqrt(number)
if sq_root*sq_root==number:
    print("The number is a Perfect square")
else:
    pass