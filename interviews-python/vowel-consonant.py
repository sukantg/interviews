# How do you calculate number of vowels and consonants in a string?

def vowcon(str):
    str = str.lower()
    vowels = set('aeiou')
    vowel = 0
    conson = 0
    for i in str:

        if i.isalpha():
            if i in vowels:
                vowel = vowel + 1
            else:    
                conson = conson + 1

    return vowel, conson

yourStr = input("Provide a string: ")
vowels, consonants = vowcon(yourStr)
print ("vowel count is " + str(vowels) + " and consonant count is " + str(consonants))