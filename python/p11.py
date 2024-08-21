# Program to Find Sum of digits of a number

number=int(input("Enter the number you want to find the sum of digits: "))
summ=0
for i in number:
    summ=summ+i
    i=i+1
print(summ)


