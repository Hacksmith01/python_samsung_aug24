#Program to accept 3 distinct numbers and find smallest among them

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

if num1 == num2 or num2 == num3 or num3 == num1:
    print("Enter three distinct numbers")
else:
    lst= []
    lst.append(num1)
    lst.append(num2)
    lst.append(num3)

    minimum_number = min(lst)
    print("The smallest of the 3 numbers is ",minimum_number)





