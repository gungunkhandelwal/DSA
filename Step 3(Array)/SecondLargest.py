# Brute force
def simpleSecondLargest(nums):
    nums.sort()  #O(nlogn +n)
    n=len(nums)
    largest=nums[n-1]
    for i in range(n-2,-1,-1): #O(n)
        if nums[i]<largest:
            return nums[i]
    return -1

# Time complexity -O(nlogn + n ) and space complexity O(1)

# Better Solution
def betterSlargest(nums):
    largest=nums[0]
    slargest=-1
    for i in nums: #O(n)
        if largest <i:
            largest=i
    for i in nums: #O(n)
        if i > slargest and i != largest:
            slargest=i
    return slargest

# Time complexity of O(2n) and space complexity O(1)

# Optimial solution
def optimalsLargest(nums):
    largest=slargest=-1
    for i in nums:
        if i > largest:
            slargest =largest
            largest=i
        elif i != largest and i >slargest:
            slargest=i
    return slargest

# Time complexity O(n) and space complexity O(1)


arr=[8,8,6,7,1]
print(simpleSecondLargest(arr))
print(betterSlargest(arr))
print(optimalsLargest(arr))