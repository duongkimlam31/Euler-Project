def miniMaxSum(arr):
    # Write your code here
    total = 0
    max_num = float('-inf')
    min_num = float('inf')
    for i in arr:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
        total += i
    print(total-max_num, total-min_num)

if __name__ == "__main__":
    miniMaxSum([1,2,3,4,5])
