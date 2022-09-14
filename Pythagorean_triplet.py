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
