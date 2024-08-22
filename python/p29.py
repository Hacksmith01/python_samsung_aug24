# Find sum of the series: n + n(2) + n(3) + ..... m terms

n = int(input("Enter the common number n you want to use in the series: "))
m = int(input("Enter the number of terms you want to find the series for: "))
sum = 0
for i in range(1, m + 1):
    sum += n*i
    i=i+1
print(sum)






