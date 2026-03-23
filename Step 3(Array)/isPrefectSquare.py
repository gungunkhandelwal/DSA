
def isPrefectSquare(n):
    # Brut force ->O(n)
    # for i in range(n):
    #     if i*i == n:
    #         return True
    #     if i*i >n:
    #         return False

    left,right=0,n
    while left <=right:
        mid=(left+right)//2
        if mid*mid >n:
            right-=1
        elif mid*mid <n:
            left+=1
        else:
            return True
    return False
        
        
    
print(isPrefectSquare(16))
print(isPrefectSquare(3))