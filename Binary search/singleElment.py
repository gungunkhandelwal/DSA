def singleElement(nums):
    n = len(nums)
    left = 0 
    right = n -1
    while left <=right:
        mid  = left +(right - left) //2
        if mid - 1 >= left and nums[mid] == nums[mid-1]:
            if (mid - left)%2 == 0:
                right = mid -2
            else:
                left = mid +1
        elif mid +1 <= right and nums[mid] == nums[mid+1]:
            if (right - mid)% 2 == 0:
                left = mid+2
            else:
                right = mid -1
        else:
            return nums[mid]
    return -1

    # n = len(nums)
    # i = 0
    # while i < n-1:
    #     if nums[i] == nums[i+1]:
    #         i+=2
    #     else:
    #         return nums[i]
    # return nums[-1]

nums=[1,1,2,2,3,4,4,8,8]
print(singleElement(nums))