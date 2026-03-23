def binarySearch(nums,left,right,target):
    while left <=right:
        mid= left +(right - left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid -1

def infinteSortedArray(nums,target):
    left = 0
    right = 1
    while nums[right] < target:
        left = right
        right = right *2
    
    return binarySearch(nums,left,right,target)

arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
k = 100
print(infinteSortedArray(arr,k))


    