def ascArray(arr, low, high, key):
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

def descArray(arr, low, high, key):
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[mid] < key:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1


def findBitonicPoint(arr, n, l, r):
    
    bitonicPoint = 0
    mid = (r + l) // 2
    
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return mid
    
    elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        bitonicPoint = findBitonicPoint(arr, n, mid, r)
    else:
        bitonicPoint = findBitonicPoint(arr, n, l, mid)
        
    return bitonicPoint

def searchBitonic(arr, n, key, index):
    
    if key > arr[index]:
        return -1
    elif key == arr[index]:
        return index
    else:
        temp = ascArray(arr, 0, index-1, key)
        if temp != -1:
            return temp
        
        return descArray(arr, index+1, n-1, key)


# def searchBitonicArray(nums,target):
#     n= len(nums)-1
#     left , right = 0, n-1

#     if n ==1: return 0

#     while left <= right:
#         mid = left + (right - left)//2

#         if mid >0 and mid < n-1:
#             if nums[mid] > nums[mid -1] and nums[mid] > nums[mid +1]:
#                 return nums[mid]
#             elif nums[mid] < nums[mid +1]:
#                 left = mid +1
#                 descArray(nums,target,left,right)
#             else: 
#                 right = mid -1
#                 ascArray(nums,target,left,right)
#         elif mid == 0 :
#             if nums[0] < nums[1]:
#                 return nums[1]
#             else:
#                 return nums[0]
#         else:
#             if nums[n-1] < nums[n-2]:
#                 return nums[n-2]
#             else:
#                 return nums[n-1]
            
arr = [-8, 1, 2, 3, 4, 5, -2, -3]
key = 1
n = len(arr)
l = 0
r = n - 1
index = findBitonicPoint(arr, n, l, r)
print(searchBitonic(arr, n, key, index))
            