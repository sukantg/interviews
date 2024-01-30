# Check if a given number is prime.

import math
number = input("Provide a number - ")
yourInput = int(number);

def isPrime(yourInput):   
    if yourInput <= 1:
        return False;
    for i in range(2,int(math.sqrt(yourInput)+1)):
        if yourInput%i == 0:
            return False
        return True



print(isPrime(yourInput))
        

