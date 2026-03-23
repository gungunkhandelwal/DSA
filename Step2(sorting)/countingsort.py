def counting_sort(arr):
    if not arr:
        return []
    # step 1 :max values from arr
    max_values=max(arr)

    # Intialize count array
    count=[0]*(max_values+1)
    
    # count the occurence of elements
    for i in arr:
        count[i] +=1
    
    # cumulative count
    output=[]
    for i in range(len(count)):
        output.extend([i]*count[i])

    return output

A=[4,2,2,8,3,3,1]
B=[-3,3,2,1,-5,-3,7,2,2]
print(counting_sort(A))
print(counting_sort(B))

# Time complexity O(K+N) where K-->size of array
# Space complexity O(K)
    