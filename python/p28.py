# Print Prime numbers between M and N (M < N)

M = int(input("Enter the number you want to initially start the series from: "))
N = int(input("Enter the number you want to end the series from: "))

if N > M:
    for number in range(M, N + 1):
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
else:
    print("Ensure that N > M.")



