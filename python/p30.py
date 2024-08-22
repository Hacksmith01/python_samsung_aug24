# Find sum of the series: 1 - n + n2 - n3 .... m terms



n = int(input("Enter the common number n you want to use in the series: "))
m = int(input("Enter the number of terms you want to find the series for: "))

sum = 0
for i in range(m):
    new_term = (-n)**i
    sum += new_term
print("Sum of the series is: ", sum)

