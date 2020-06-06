# 002. Write a program in which lowercase letters should come first for a given string.
print("Program in which lowercase letters should come first for a given string.")
inputString=input("Enter String: ")
while inputString.__len__()==0:
    inputString=input("Enter String or ctrl+c to exit program: ")
print('Processing "'+inputString+'"')
processedString=''
for character in inputString:
    if character.islower():
        processedString=character+processedString
    else:
        processedString+=character
print('Processed string is "'+processedString+'"')
