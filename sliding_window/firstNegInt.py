from collections import deque

def firstNegInt(arr,k):
    n=len(arr)
    i=0
    result=[]
    negs=deque()
    for j in range(n):
        if arr[j]<0:
            negs.append(j)
        
        if (j-i+1)==k:
            if negs and negs[0] >=0:
                result.append(arr[negs[0]])
            else:
                result.append(0)
            
            if negs and negs[0]==i:
                negs.popleft()
            i+=1
    return result


# arr=[-8, -22, 3, -6, 10]
arr=[12 ,-1, -7, 8, -15, 30, 16, 28]
k=3
print(firstNegInt(arr,k))

# Time complexity -O(n) and space complexity-O(n)