def nth_prime(n):
    count = 0
    prime = 0
    num = 1
    while count < n:
        if isprime(num) == True:
            count += 1
            prime = num
            num += 1
        else:
            num += 1
    return prime

def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
