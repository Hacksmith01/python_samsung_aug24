# Find Nth Fibo term (assume 1 and 2 as 1st 2 terms)

number=int(input("Enter the number of terms you want to find the Nth fibo series number from: "))

a , b = 1 , 2
if number == 1:
    print(a)
elif number == 2:
    print(b)
else:
    for i in range(3, number+1):
        a , b  = b , a+b

    print(b)







