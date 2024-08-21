# Program to Print Math table of a number

number = int(input("Enter the number you want to find the table of: "))
rang=int(input("Enter the range till where you want to find the multiples: "))

for i in range(rang+1):
    print(f"{number} x" ,i,"==",number*i)
    i=i+1