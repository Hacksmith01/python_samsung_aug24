
#using dictionary
import math

customer_bills = {}

N = int(input("Enter the number of customers: "))

for i in range(N):
    customer_id = int(input("Enter the ID of customer: ")) 
    bill_amount = int(input("Enter the bill of customer: "))
     
    customer_bills[customer_id] = bill_amount
 
print("Customer bills dictionary:", customer_bills)


for customer_id, bill_amount in customer_bills.items():
    root = int(math.sqrt(bill_amount))
    
    if root * root == bill_amount:
        print(f"The person with ID {customer_id} got a promotional code.")
    else:
        print(f"Sorry, the person with ID {customer_id} does not get a promotional code.")








