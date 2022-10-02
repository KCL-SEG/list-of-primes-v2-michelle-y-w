"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def isPrime(num):
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'number of primes: {number_of_primes} must be larger than 0')
    list = []
    cnt = 0
    num = 2
    while cnt < number_of_primes:
        if isPrime(num):
            cnt += 1
            list.append(num)
        num += 1
    return list
