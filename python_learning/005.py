# 005. Write a program to display the fibonnaic series from 0 to 100
def getFibonacci(limit):
    series=[0,1,1]
    next=series[series.__len__()-2]+series[series.__len__()-1]
    while next < limit:
        series.append(next)
        next=series[series.__len__()-2]+series[series.__len__()-1]
    return series

print("Program to print fibonacci series upto limit.")
limit=""
while not limit.isnumeric():
    limit=input("Enter upper limit of fibonacci series: ")
fibonacciSeries=[]
print("Generating series...")
fibonacciSeries=getFibonacci(int(limit))
print(fibonacciSeries.__str__())