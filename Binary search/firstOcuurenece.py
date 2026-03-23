def binarySearch(nums,left,right):
    res = -1
    while left <= right:
        mid = left +(right - left)//2
        if nums[mid] == 1:
            res = mid
            right = mid -1
        elif nums[mid] < 1:
            left = mid + 1
        else:
            right = mid -1
    return res


def inifinteArray(nums):
    left = 0
    right = 1

    while nums[right] < 1:
        left = right
        right = right * 2

        return binarySearch(nums, left, right)
    
arr=[0, 0, 1, 1, 1, 1]
print(inifinteArray(arr))