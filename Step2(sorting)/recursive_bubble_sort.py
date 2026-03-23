def recursive_bubble_sort(arr,n):
    if n==1:
        return
    
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
    
    recursive_bubble_sort(arr,n-1)

    return arr

A=[-3,3,2,1,-5,-3,7,2,2]
print(recursive_bubble_sort(A,9))

# Time complexity O(n^2)
# Space complexity O(N)