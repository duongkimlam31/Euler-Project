'''
Question: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def sum(n):
    sum = 0
    num = 2
    while num < n:
        if isprime(num) == True:
            sum += num
            num += 1
        else:
            num += 1
    return sum


def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
