def moveZeros(nums):
    if not nums:
        return 0
    last_zero=0 #left pointer
    for i in range(len(nums)): #right pointer
        if nums[i] != 0:
            nums[last_zero],nums[i]=nums[i],nums[last_zero]
            last_zero +=1
    return nums

    

A=[0,1,0,3,12]
print(moveZeros(A))

# Approach 2 pointers t.c O(n) and s.c O(1)