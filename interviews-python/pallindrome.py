# How do you determine if a string is a palindrome?

def pallindromeCheck1(str):
    for i in range(len(str) // 2):
        if str[i] != str[len(str)-1-i]:
            return False
        return True

def pallindromeCheck2(str):
    return str == str[::-1]        

yourString = input("Please provide a string - ")  
print (pallindromeCheck1(yourString)) 
print (pallindromeCheck2(yourString))     
