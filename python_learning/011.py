# 011. Write a program to find whether a given number is Armstrong number or not.
def isArmstrong(number):
    armstrong=True
    sum=0
    for character in str(number):
        sum+=int(character) ** str(number).__len__()
    armstrong=(sum==number)
    return armstrong

number=""
while not number.isnumeric():
    number=input("Enter number to check armstrong: ")
print("Processing...")
if isArmstrong(int(number)):
    print(number+" is armstrong.")
else:
    print(number+" is not armstrong.")