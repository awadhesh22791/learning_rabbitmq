# 011. Write a program to find armstrong number till given limit.
def isArmstrong(number):
    armstrong=True
    sum=0
    for character in str(number):
        sum+=int(character) ** str(number).__len__()
    armstrong=(sum==number)
    return armstrong

number=""
while not number.isnumeric():
    number=input("Enter the limit to find armstrong number: ")
print("Processing...")
i=0
armstrong=[]
while i<=int(number):
    if isArmstrong(i):
        armstrong.append(i)
    i+=1
if armstrong.__len__()>0:
    print("Armstrong number till "+number+" are "+armstrong.__str__())
else:
    print("No any armstrong number available till "+number)