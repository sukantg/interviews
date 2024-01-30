# Find if two strings are anagrams.

def anagramCheck(str1,str2):
    return sorted(str1) == sorted(str2)

String1 = input("Please provide first string :")
String2 = input("Please provide second string:")

if(anagramCheck(String1,String2)):
    print ("They are anagrams")
else:    
    print("Not anagrams")    
