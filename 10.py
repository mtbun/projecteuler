#10.

def primes(number):
    prime = True
    for y in range(2,number):
        if number%y ==0:
            prime = False
    return prime

def primessum(number):
    sum = 0
    for x in range(2,number):
        if primes(x):
            sum += x
    return sum

print(primessum(2000000))