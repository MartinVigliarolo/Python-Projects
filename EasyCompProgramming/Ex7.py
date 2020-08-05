# Get prime factor of a number

import math

def is_prime(prime):
    for i in range(2, math.ceil(math.sqrt(prime))+1):
        if(prime % i == 0) and (i != prime):
            return False
    return True

def find_next_prime(num,prime):
    prime = prime + 1
    while (not is_prime(prime)):
        prime += 1
    return prime


def get_prime_factor(num):
    ret = []
    prime = 2
    while num != 1:
        while (int(num) % prime) != 0:
            prime = find_next_prime(num,prime)
        num = int(num)/prime
        ret.append(int(prime))
    return ret

try:
    num = int(input("Enter any integer number to get its prime factor descomposition:"))
    prime_list = get_prime_factor(num)
    print(prime_list)
except:
    print("The input must be an integer")