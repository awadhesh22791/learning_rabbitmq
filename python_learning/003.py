# 003. Given a two list of int’s create a third list such that should contain only odd numbers from the first 
# list and even numbers from the second list
def getList(numberOfElements):
    i=0
    list=[]
    while i in range(numberOfElements):
        number=''
        while not number.isnumeric():
            number=input("Enter element number "+i.__str__()+":")
        i+=1
        list.append(int(number))
    return list

firstList=secondList=thirdList=[]
print("Given a two list of int’s create a third list such that should contain only odd numbers from the first listand even numbers from the second list")
number=""
while not number.isnumeric():
    number=input("Enter length of list: ")
number=int(number)
print("Enter 4 values for first list:\n")
firstList=getList(number)
print("Enter 4 values for second list:\n")
secondList=getList(number)
print("Processing first list: "+firstList.__str__())
for value in firstList:
    if value % 2 != 0:
        thirdList.append(value)
print("Processing second list: "+secondList.__str__())
for value in secondList:
    if value % 2 == 0:
        thirdList.append(value)
print("Processed list: "+thirdList.__str__())
