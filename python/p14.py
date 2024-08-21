# Program to find 2nd smallest digit in a number

number = input("enter the number in which you want to find the 2nd smallest number: ")

lst_num=list(number)
print(lst_num)

lst_num.sort()
print("The 2nd smallest digit in the number in the list is: ",lst_num[1])


