def recursive_insertion_sort(arr,n):
    if n == 1:
        return
    
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]> arr[j]:
                arr[j-1],arr[j]= arr[j],arr[j-1]

    recursive_insertion_sort(arr,n-1)

    return arr

A=[-3,3,2,1,-5,-3,7,2,2]
print(recursive_insertion_sort(A,9))


# Space complexity O(N)
# Time complexity O(N^3) --> not efficient


def recursive_insert_sort(arr,n):
    if n <=1:
        return
    
    recursive_insert_sort(arr,n-1)

    last=arr[n-1]
    j=n-2

    while j >=0 and arr[j] >last:
        arr[j+1] = arr[j]
        j -=1
    
    arr[j+1]=last

    return arr

B=[-3,3,2,1,-5,-3,7,2,2]
print(recursive_insert_sort(B,9))

# Time complexity O(n^2) 