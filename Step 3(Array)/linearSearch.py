def linearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

A=[2, 3, 4, 5, 3]
k=3
B=[2, -4, 4, 0, 10]
l=6
print(linearSearch(A,k))
print(linearSearch(B,l))

# brute force Time complexity O(n) and space complexity O(1)

