# 009. Write a program in which the function should take an input as a parameter in which the function should 
# calculate the factorial of a given number.
def factorial(number):
    factorial=1
    i=1
    while i <=number:
        factorial*=i
        i+=1
    return factorial

number=""
while not number.isnumeric():
    number=input("Enter number to calculate factorial: ")
print("Calculating factorial of "+number)
factorialOfNumber=factorial(int(number))
print("Factorial of "+number.__str__()+" is "+factorialOfNumber.__str__())