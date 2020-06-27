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

def getCorrectZeros(digits):
    init = 10
    for i in range(digits-1):
        init = init*10
    return init

def buscarPalindromo(ent,digits):
    if int(digits) == 1:
        return ent
    else:
        digitoMenor = int(ent) % 10
        if int(digits) == 2:
            digitoMayor = math.floor(int(ent)/10)
            if digitoMenor > digitoMayor:
                return str(digitoMayor + 1) + str(digitoMayor + 1)
            else:
                return str(digitoMayor) + str(digitoMayor)
        else:
            unoConCerosCorrectos = getCorrectZeros(digits-1)
            digitoMayor = math.floor(int(ent)/(unoConCerosCorrectos))
            if digitoMayor < digitoMenor:
                ent = int(ent) + 10 - (digitoMenor - digitoMayor)                
            ent =  int(ent) - digitoMayor*unoConCerosCorrectos
            ent = math.floor(int(ent)/10)
            return str(digitoMayor) + str(buscarPalindromo(ent,digits-2)) + str(digitoMayor)
    

t = input()
entradas = []

for i in range(int(t)):
    entradas.append(input())

for ent in entradas:
    digits = getDigits(ent)
    print(buscarPalindromo(ent,digits))