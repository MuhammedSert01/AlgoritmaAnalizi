def maxSubSum(vector):
    max_last = 0
    maxSum = 0
    for i in vector:
        max_last = max(0, max_last + i)
        maxSum = max(maxSum, max_last)
    return maxSum
array = [4, -3, 5, -2, -1, 2, 6, -2]
print(maxSubSum(array))
