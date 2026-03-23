from math import inf


def maxSumofArray(arr,k):
    n=len(arr)
    i,j=0,0
    window_sum=0
    max_sum= float(-inf)
    while j<n:
        window_sum=window_sum+arr[j]
        if (j-i+1) <k:
            j+=1
        elif(j-i+1) == k:
            max_sum=max(max_sum,window_sum)
            window_sum=window_sum-arr[i]
            i+=1
            j+=1
    return max_sum

nums = [1, 2, 3, 4, 5]
k = 2
nums1 = [5, 2, 9, 1, 7]
k1 = 1
nums2 = [3, 4, 2, 1]
k2 = 4
nums3 = [2, -1, 3, -4, 5, -2, 6]
k3 = 3
nums4 = [-3, -1, -2, -4, -6]
k4= 2
print(maxSumofArray(nums,k))
print(maxSumofArray(nums1,k1))
print(maxSumofArray(nums2,k2))
print(maxSumofArray(nums3,k3))
print(maxSumofArray(nums4,k4))





