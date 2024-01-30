# Find number of occurrences of a string character in a string.

def occurences1(char,str):
    count = 0
    for i in str:
        if (i == char):
            count = count + 1
    return count        

def occurences2(char,str):
    return str.count(char)

yourString = input("Please provide a string:")
yourCharacter = input("Character to check:")

print(occurences1(yourCharacter,yourString))
print(occurences2(yourCharacter,yourString))


