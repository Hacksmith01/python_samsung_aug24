no = int(input("Enter the number memory to be allocated: "))


server_1=[]
server_2=[]
for i in range(no):
    N = int(input("Enter the memory to be allocated in server_1: "))
    if N%2==0:
        server_1.append(N)
    else:
        pass
    NA = int(input("Enter the memory to be allocated in server_2: "))
    if NA%2==0:
        server_2.append(NA)
    else:
        pass

sum1=sum(server_1)
sum2=sum(server_2)
if sum1%2==0:
    print("The memory has to be allocated")
else:
    print("The sum has to be delocated")








