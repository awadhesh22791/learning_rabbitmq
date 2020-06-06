# 007. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then 
# check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma 
# separated sequence.
inputString=""
digitArray=[]
numberDivisibleBy5=[]
while inputString.__len__()==0:
    inputString=input("Enter comma separated digits: ")
    digitArray=inputString.split(",")
    for character in digitArray:
        if not character.isnumeric():
            print("Your string '%s' contains non numeric value."%(inputString))
            inputString=""
            break
        else:
            if int(character) % 5 == 0 :
                numberDivisibleBy5.append(int(character))
print("Digit array is %s"%(digitArray.__str__()))
print("Processed array is %s"%(numberDivisibleBy5.__str__()))