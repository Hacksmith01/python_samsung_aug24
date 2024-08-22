# Assume 1 and 2 are 1st 2 terms of the series and print the 1st N term of Fibo series (HemaChandra numbers)

Number = int(input("Enter the number of terms you want to find the fibonacci series of : "))

a, b = 1, 2
for i in range(Number):
    print(a, end=' ')
    a, b = b, a + b
print()













