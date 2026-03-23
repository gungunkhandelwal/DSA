def findFloor(nums,x):
    left,right=0,len(nums)
    ans=-1
    while left <= right:
        mid=(left+right)//2
        if nums[mid] <= x:
            ans=nums[mid]
            left=mid+1
        else:
            right=mid-1

    return ans

def findCeil(nums,x):
    left,right=0,len(nums)
    ans=-1
    while left <= right:
        mid=(left+right)//2
        if nums[mid] >= x:
            ans=nums[mid]
            right=mid-1
        else:
            left=mid+1

    return ans

def floorAndCeil(nums,x):
    f=findFloor(nums,x)
    c=findCeil(nums,x)
    return f,c
    

A=[3, 4, 4, 7, 8, 10]
x=5
print(floorAndCeil(A,x))
        