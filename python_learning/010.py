# 010. Define a function which can generate and print a list where the values are square of numbers between 1 
# and 20
inputString=""
digitArray=[]
result=[]
while inputString.__len__()==0:
    inputString=input("Enter comma separated digits: ")
    digitArray=inputString.split(",")
    for character in digitArray:
        if not character.isnumeric():
            print("Your string '%s' contains non numeric value."%(inputString))
            inputString=""
            break
        else:
            squareRootOfNumber=int(int(character) ** (1/2))
            if squareRootOfNumber > 1 and squareRootOfNumber < 20 :
                result.append(int(character))
print("Digit array is %s"%(digitArray.__str__()))
print("Processed array is %s"%(result.__str__()))