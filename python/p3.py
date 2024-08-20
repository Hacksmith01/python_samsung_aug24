'''Accept a number as input, say "x" and define logic to get the ouput "y". 
The input can only be 0 and 1 and the output must be 1 if input 0 and vice-versa. Do not use bolean'''

x=int(input("enter the number(either 0 or 1): "))

#To check whether the input is 0 or 1
if x==0 or x==1:
    y=1-x
    print(f"input number is {x} : output number is {y}")
else:
    print("Invalid input, enter 0 or 1")
