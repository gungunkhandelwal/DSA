def maxConsecutive(nums):
    # Appraoch 1: simple
    # count=0
    # res=0
    # for i in nums:
    #     if i ==0:
    #         count=0
    #     else:
    #         count+=1

    #     if res<count:
    #         res =count
    # return res
    
    # Approach 2: Sliding window
    res=0
    left=0
    for right in range(len(nums)):
            if nums[right] == 0:
                left =right+1
            
            else:
                res=max(res,right-left+1)
    return res

n=[1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,1]
print(maxConsecutive(n))

# Both approach has time complexity of O(N) and space complexity O(1)