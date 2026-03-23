def maxBitonicArray(nums):
    n= len(nums)-1
    left , right = 0, n-1

    if n ==1: return 0

    while left <= right:
        mid = left + (right - left)//2

        if mid >0 and mid < n-1:
            if nums[mid] > nums[mid -1] and nums[mid] > nums[mid +1]:
                return nums[mid]
            elif nums[mid] < nums[mid +1]:
                left = mid +1
            else: 
                right = mid -1
        elif mid == 0 :
            if nums[0] < nums[1]:
                return nums[1]
            else:
                return nums[0]
        else:
            if nums[n-1] < nums[n-2]:
                return nums[n-2]
            else:
                return nums[n-1]
            
A=[1,3,8,12,4,2]
print(maxBitonicArray(A))

A1=[5,10,15,20,25,30,35,40,45,50,4,3,2,1,]
print(maxBitonicArray(A1))
            