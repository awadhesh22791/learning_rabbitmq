# 6.	Write a program to display the following * pattern
#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * *
number=""
while not number.isnumeric():
    number=input("Enter limit to print pattern: ")
number=int(number)
for i in range(number):
    for j in range(number-i):
        print(" ",end="")
    k=0
    for k in range(i+1):
        print("* ",end="")
        k+=1
    print("")