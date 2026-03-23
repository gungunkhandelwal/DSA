def nearestLargest(arr):
    result=[]
    stack=[]
    n=len(arr)

    for i in range(n):
        while len(stack) >0 and stack[-1] < arr[i]:
            stack.pop()
        
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        stack.append(arr[i])
    return result

A=[1,3,2,4]
print(nearestLargest(A))