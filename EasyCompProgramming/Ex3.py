# A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.
# Input

# The first line contains integer t, the number of test cases. Integers K are given in the next t lines.
# Output

# For each K, output the smallest palindrome larger than K.
# Example

# Input:
# 2
# 808
# 2133

# Output:
# 818
# 2222

import math

def getDigits(ent):
    return math.floor(math.log(int(ent),10)+1)

t = input()
entradas = []

for i in range(int(t)):
    entradas.append(input())

for ent in entradas:
    digits = getDigits(ent)
    ret = ''
    if digits == 1:
        print(ent)
    else:
        while digits > 1:
            digitoMayor = math.floor(int(ent)/10*(digits-1))
            # digitoMenor = 
            ret = str(digitoMayor) + ret + str(digitoMayor)
            digits = digits - 2
        print(ret)



