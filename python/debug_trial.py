'''
def find_factorial_iteratively(num):
    factorial_number = 1
    if num ==0 or num ==1:
        return factorial_number
    for i in range(2, num+1):
        factorial_number = factorial_number * i

   


def find_factorial_recursively(num):
    if num ==0 or num ==1:
        return 1
    return num * find_factorial_recursively(num - 1)

input_number=int(input("Enter a number to find its factorial: "))

ch = int(input("choose your choice:\n1.iteratively\n2.recursively"))
factorial_number = 0

if ch == 1:
    factorial_number = find_factorial_iteratively(input_number) 
else:
    factorial_number = find_factorial_recursively(input_number) 

print(f'factorial of {input_number} = {factorial_number}')

'''









import pdb
pdb.set_trace()

def sum_digits(num):
    sum=0
    while num != 0:
        remainder=num%10
        num = num // 10
        sum+= remainder
    return sum

input_number=int(input("Enter a number to find su of digits: "))
summ=sum_digits(input_number)
print(f'sum of digits of {input_number} = {summ}')+


