# 004. Given a string you should check a whether it is Palindrome or Not
inputString=""
print("Program to check string is palindrop or not.")
while inputString.__len__()==0:
    inputString=input("Enter string to check: ")
reverseString=""
for character in inputString:
    reverseString=character+reverseString
if inputString.__eq__(reverseString):
    print('Your string "'+inputString+'" is palindrome.')
else:
    print('Your string "'+inputString+'" is not palindrome.')
