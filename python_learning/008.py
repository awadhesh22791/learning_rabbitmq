# 008. Write a program for finding out the transpose of Matrix A
#Note: consider matrix (2,2)

number=""
while not number.isnumeric():
    number=input("Enter limit of matrix: ")
rows=columns=int(number)
matrix=[[0 for row in range(rows)] for column in range(columns)]
for row in range(rows):
    for column in range(columns):
        value=""
        while not value.isnumeric():
            value=input("Enter value for [%i] [%i]:"%(row,column))
        matrix[row][column]=int(value)
print("Transposing %s"%(matrix.__str__()))
for row in range(rows):
    for column in range(columns):
        if row > column:
            matrix[row][column]=matrix[row][column] + matrix[column][row]
            matrix[column][row]=matrix[row][column] - matrix[column][row]
            matrix[row][column]=matrix[row][column] - matrix[column][row]
print("Transposed matrix: %s"%{matrix.__str__()})