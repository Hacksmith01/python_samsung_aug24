#Read a number from the user and check if it is an Even number or not
my_number=int(input("Enter the number to check if the number is even or not an even number: "))
if my_number%2==0:
    print(f"{my_number} is Even")
else:
    print(f"{my_number} is not an Even number")