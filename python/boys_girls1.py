t=int(input("Enter the numner of test cases:"))
n=int(input("Enter the uumber ofboys and girls: "))

boys=[]
for i in range(n):
    boyh=int(input("Enter the boys height: "))
    boys.append(boyh)
boys.sort()
girls=[]
for i in range(n):
    girlh=int(input("Enter the girls height: "))
    girls.append(girlh)
girls.sort()

final=[]
i=0
for i in girls:
    for k in boys:
        final.append(k)
        k=k+2
    final.append(i)
    i=i+2


print(final)



