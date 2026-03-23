def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    
    pivot=arr[-1]
    L=[x for x in arr[:-1] if x<=pivot]
    R=[x for x in arr[:-1] if x > pivot]

    return quick_sort(L)+[pivot]+quick_sort(R)

A=[-3,3,2,1,-5,-3,7,2,2]
print(quick_sort(A))


# Time complexity of O(NlogN) and space complexity O(N)