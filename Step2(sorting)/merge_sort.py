# Merge sort Time complexity:O(NlogN). space complexity:O(N)

def merge_sort(arr):
    n=len(arr)
    if n==1:
        return arr
    
    mid=len(arr)//2
    L=arr[:mid]
    R=arr[mid:]

    # Divide left and right array
    L=merge_sort(L)
    R=merge_sort(R)
    l,r=0,0
    L_len=len(L)
    R_len=len(R)

    sorted_arr=[]
    # i=0

    while l<L_len and r<R_len:
        if L[l] <R[r]:
            sorted_arr.append(L[l])
            l+=1
        else:
            sorted_arr.append(R[r])
            r+=1
        # i+=1
    
    while l<L_len:
        sorted_arr.append(L[l])
        l+=1
        # i+=1
    
    while r<R_len:
        sorted_arr.append(R[r])
        r+=1
        # i+=1
    
    return sorted_arr


A=[-5,3,2,1,-3,-3,7,2,2]
print(merge_sort(A))

