# Program to Print X shape inside Hollow Square

lines=int(input("Enter the number of lines you want to print X: "))

for i in range(1,lines+1):
    for j in range(1,lines+1):
        if j == 1 or j == lines or i == j or j == lines - i + 1:
            print("* ", end='')
        else:
            print("  ",end='')
    print()

