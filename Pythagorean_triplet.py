'''
Question: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math
def solution(n):
    a = 1
    b = 2
    c = math.sqrt((a**2)+(b**2))
    while a < n:
        while b < n:
            if a + b + c == n:
                print(a,b,c)
                return a*b*c
            else:
                b += 1
                c = math.sqrt((a**2)+(b**2))
        a += 1
        b = a + 1
        c = math.sqrt((a**2)+(b**2))
    if a + b + c == n:
        print(a,b,c)
        return a*b*c
    else:
        return - 1

if __name__ == "__main__":
    print(solution(1000))