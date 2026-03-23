def lowerBound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

A=[1,2,2,3]
x=2
A1=[3,5,8,15,19]
x1=9
print(lowerBound(A1,x1))
print(lowerBound(A,x))