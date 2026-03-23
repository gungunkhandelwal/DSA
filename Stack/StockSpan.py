def stockSpan(arr):
    n=len(arr)
    result=[]
    stack=[]

    for i in range(n):
        while len(stack) > 0 and stack[-1][0] <= arr[i]:
            stack.pop()
        
        if not stack:
            result.append(-1)
        
        else:
            result.append(stack[-1][1])
        
        stack.append((arr[i],i))
    
    for i in range(len(result)):
        result[i] = i - result[i]

    return result

A=[100,80,60,70,60,75,85]
print(stockSpan(A))
