# Program to find biggest (smallest) digit in a number

number = input("Enter a number you want to find the largest and smallesst number from : ")

large_digit = '0'
small_digit = '9'

for char in number:
    if char.isdigit():
        if char > large_digit:
            large_digit = char
        if char < small_digit:
            small_digit = char

print("Largest digit:", large_digit)
print("Smallest digit:", small_digit)










