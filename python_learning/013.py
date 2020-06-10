# Program to check two strings are anagram or not
# For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.
print("Program to check two strings are anagram or not.")
def getStr(message):
    inputString=""
    while inputString.__len__()==0 and inputString.__len__() <=100:
        inputString=input(message)
    inputString=inputString.lower()
    return inputString

firstString=getStr("Enter first String: ")
secondString=getStr("Enter second String: ")
anagram=True
if firstString.__len__()==secondString.__len__():
    for c in firstString:
        if firstString.count(c)!=secondString.count(c):
            anagram=False
            break
else:
    anagram=False
if anagram :
    print("Anagram")
else:
    print("Not Anagram")
