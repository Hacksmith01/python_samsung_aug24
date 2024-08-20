# Program to check if the alphabet is Vowel or Consonant

alpha=input("Enter the alphabet you want to check is a vowel or a consonant: ")
if len(alpha)==1:
    if alpha in "aeiou":
        print("The alphabet is a vowel")
    else:
        print("The alphabet is a consonant")
else:
    pass
