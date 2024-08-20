#Program to check if the alphabet is uppercase

alphabet = input("Enter the alphabet: ")

if len(alphabet) == 1 and alphabet.isupper():
    print("Yes the alphabet is in uppercase")
else:
    print("No  the alphabet is not in uppercase")
