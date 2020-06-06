# 001. Write a program to Count all lowercase, uppercase, digits, and special symbols for a given string.

print("Program to Count all lowercase, uppercase, digits, and special symbols for a given string.")
inputString=input("Enter String: ")
while inputString.__len__()==0:
    inputString=input("Enter String or ctrl+c to exit program: ")
print('Processing "'+inputString+'"')
lowercase=uppercase=digits=specialSymbols=0
for character in inputString:
    if character.isupper():
        uppercase+=1
    elif character.islower():
        lowercase+=1
    elif character.isdigit():
        digits+=1
    else:
        specialSymbols+=1
print("String analysis is below:")
print(lowercase.__str__()+" Lower case characters")
print(uppercase.__str__()+" Upper case characters")
print(digits.__str__()+" Digits")
print(specialSymbols.__str__()+" Special symbols")
    