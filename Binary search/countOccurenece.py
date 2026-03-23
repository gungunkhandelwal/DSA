def countOccurenece(arr,x):
    # count=0
    # for i in arr:
    #     if i == x:
    #         count +=1
    # return count
    def firstOccurence():
        count=-1
        left,right=0,len(arr)
        while left <=right:
            mid =(left+right)//2
            if arr[mid] == x:
                count=mid
                right=mid-1
            elif arr[mid] <x:
                left=mid+1
            else:
                right=mid-1
        return count
    
    def lastOccurence():
        count=0
        left,right=0,len(arr)
        while left <=right:
            mid=(left+right)//2
            if arr[mid] == x:
                count=mid
                left=mid+1
            elif arr[mid] < x:
                left=mid+1
            else:
                right=mid-1
        return count
    total= lastOccurence() - firstOccurence()+1
    return total


arr=[2,2,3,3,3,3,4,5]
x=3
print(countOccurenece(arr,x))