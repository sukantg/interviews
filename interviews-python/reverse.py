original = input("Please provide a string - ")

reversed1 = original[::-1]
print (reversed1)

reversed2 = ''
for char in original:
    reversed2 = char + reversed2

print (reversed2)    

