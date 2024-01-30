##How do you remove all occurrences of a character from a string?

def remove(str,char):
    removed = ''
    for i in str:
        if char!=i:
            removed = removed + i
    return removed
    
initial = input("Your string : ")
char = input("Your character: ")
print(remove(initial,char))