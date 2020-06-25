#  Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!
# Input

# The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.
# Output

# For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

import math

t = input()
pares = []

for i in range(int(t)):
    pares.append(input())

for par in pares:
    m, n = par.split()
    m = int(m)
    n = int(n)
    for num in range(m,n):
        raiz = math.floor(math.sqrt(num))
        j = 1
        esPrimo = True
        while esPrimo and j < raiz:
            j += 1
            if (num % j) == 0:
                esPrimo = False
        if esPrimo:
            print(num)
    print("\n")
              
    
    