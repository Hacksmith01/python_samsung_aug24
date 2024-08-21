'''
Program to print the Equi Lateral Triangle of N lines
    *
   ***
  *****
 *******
*********
'''
number = int(input("Enter the number of lines for the Equilateral Triangle: "))

for i in range(number):
    print(' ' * (number - i - 1), end='')
    print('*' * (2 * i + 1))




