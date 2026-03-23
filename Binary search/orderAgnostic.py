def orderAgnostic(arr,target):
    def ascendingSearch():
        left, right= 0,len(arr)-1
        while left <= right:
            mid= left+(right - left)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left=mid+1
            else:
                right=mid-1
        return -1

    def descendingSearch():
        left, right= 0,len(arr)-1
        while left <= right:
            mid= left+(right - left)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                right = mid -1
            else:
                left = mid +1 
        return -1

    n=len(arr)
    if n ==1 and arr[0] == target :
        return n
    

    if arr[0] < arr[-1]:
        return ascendingSearch()
    else :
        return descendingSearch()


A=[1,2,3,4,5,6,7,8,9,10]
target=2
print(orderAgnostic(A,target))

A2=[10,9,8,7,6,5,4,3,2,1]
target2=2
print(orderAgnostic(A2,target2))


        