# Program to print X shape of N lines

number_of_lines = int(input('Enter number of lines to draw the star shape: '))

for i in range(number_of_lines):
    for j in range(number_of_lines):
        if j == i or j == number_of_lines - i - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()



