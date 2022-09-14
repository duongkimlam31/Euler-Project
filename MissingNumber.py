def missing_number(n, list):
    for i in range(n):
        if i not in list:
            break;
    print(i)
    return i
