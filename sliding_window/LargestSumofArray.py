from math import inf

def largestSumofArray(nums,k):
    n=len(nums)
    i,j=0,0
    window_sum=0
    max_size=float(-inf)
    while j<n:
        window_sum += nums[j]

        while window_sum > k and i <= j:
            window_sum -= nums[i]
            i += 1

        if window_sum == k:
            max_size = max(max_size, j - i + 1)

        j += 1

    return max_size if max_size > 0 else -1 

A=[4,1,1,1,2,3,5]
k=5
A1 = [10, -10, 10, -10, 10]
k1 = 10
A2 = [1, 2, 3, 7, 5]
k2 = 12
A3 = [5, 5, 5, 5]
k3 = 5
print(largestSumofArray(A,k))
print(largestSumofArray(A1,k1))
print(largestSumofArray(A2,k2))
print(largestSumofArray(A3,k3))