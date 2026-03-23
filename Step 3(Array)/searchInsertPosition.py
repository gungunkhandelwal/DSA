def searchInsert(nums,target):

    # approach1: Binary search +condition T.c: O(logn),s.c:O(1)
    def condition(value):
        return nums[value] >=target
    
    left,right=0,len(nums)
    while left<right:
        mid=left+(right-left)//2
        if condition(mid):
            right=mid
        else:
            left=mid+1
    return left

    # Approach 2:Brute force T.c:O(n),s.c:O(1)
    # for i in range(len(nums)):
    #     if nums[i] >=target:
    #         return i
    # return i+1

A=[1,3,5,6]
target=5
print(searchInsert(A,target))