def minimumElement(nums,target):
    left , right = 0 , len(nums) -1
    while left <= right :
        mid = left +(right - left)//2

        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    if abs(target - nums[left]) < abs(target - nums[right]):
        return nums[left]
    else:
        return nums[right]
    
A=[1,3,8,10,12,15]
target=12
print(minimumElement(A,target))