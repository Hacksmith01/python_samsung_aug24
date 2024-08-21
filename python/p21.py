# Program to print a Hollow Square of N lines

N=int(input("Enter the nummber: "))

print(N*"*"+" ")
for i in range(N - 2):
    print('*' + ' ' * (N - 2) + '*')
print(N*"*"+" ")







