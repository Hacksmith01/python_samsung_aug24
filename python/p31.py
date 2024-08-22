# Find sum of the sries: n - n2/3 + n4/5 - n8/7 .... m terms (1<m<10)

n = int(input("Enter the common number as n : "))
m = int(input("Enter the number of terms as m : "))

if 1 < m < 10:
    sum_series = 0
    for k in range(m):
        term = ((-1) ** k) * (n ** (2 ** k)) / (2 * k + 1)
        sum_series += term
    print("The sum of the series is:", sum_series)
else:
    print("Enter number in proper range.")






