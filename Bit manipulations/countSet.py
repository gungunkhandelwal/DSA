def countSet(n):
    # Time complexity -> O(log n) and space complexity -> O(log n)
    count = 0
    while n > 0:
        count += n&1
        n = n >> 1

    return count

n = 16
print(countSet(n))