def bubble_sort(arr):
    n=len(arr)
    flag=True
    while flag:  #does not loop to n 
        flag=False
        for i in range(1,n):   #only count this for t.c 
            if arr[i-1] >arr[i]:
                flag=True
                arr[i],arr[i-1]=arr[i-1],arr[i]
    return arr

A=[-5,3,2,1,-3,-3,7,2,2]
print(bubble_sort(A))

# Time complexity : O(n) and space complexity:O(1)