def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break
    
    return arr

A=[-5,3,2,1,-3,-3,7,2,2]
print(insertion_sort(A))

# Time complexity of O(N^2). and space complexity O(1)

'''
Best Case Time Complexity: 
The best case occurs if the given array is already sorted. 
And if the given array is already sorted, the outer loop will only run and the inner loop will run for 0 times. 
So, our overall time complexity in the best case will boil down to O(N), where N = size of the array.
'''