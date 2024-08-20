'''Accept average score from the student of his exam and print his result as follows:
0 to 49 : fail
50 to 74 : 2nd class
75 to 90 :1st class
91 to 100 : distinction'''

exam1=int(input("Enter the marks of exam 1: "))
exam2=int(input("Enter the marks of exam 2: "))
exam3=int(input("Enter the marks of exam 3: "))
avg=(exam1+exam2+exam3)/3

if 0<=avg<=49:
    print("fail")
elif avg<=74:
    print("2nd class")
elif avg<=90:
    print("1st class")
elif avg<=100:
    print("distinction")
else:
    print("Enter appropriate score")







