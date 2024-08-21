# Check if a number is Prime

number = int(input("Enter the number you want to check if it's a prime number: "))
if number <= 1:
    print(f"The number {number} is not a prime number.")
elif number == 2:
    print(f"The number {number} is a prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"The number {number} is not a prime number.")
            break
    else:
        print(f"The number {number} is a prime number.")




