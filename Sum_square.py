def difference(n):
    sum_square = 0
    square_sum = 0
    for i in range(1, n + 1):
        sum_square += i**2
    for i in range(1, n + 1):
        square_sum += i
    return square_sum**2 - sum_square
