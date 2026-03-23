def containDuplicate(nums,k):
        # Brute force Time complexity-O(n^2) & s.c-O(1)
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j] and i !=j and abs(i-j)<=k:
                    return True
        return False

        # Hash set T.c-O(n) & s.c-O(min(n,k))
        # seen=set()
        # for i,x in enumerate(nums):
        #     if x in seen:
        #         return True
            
        #     seen.add(x)
        #     if i>=k:
        #         seen.remove(nums[i-k])
        # return False

        # Hash map T.c-O(n) & s.c-O(n)
        # last_index={}
        # for i,x in enumerate(nums):
        #     if x in last_index and i-last_index[x]<=k:
        #         return True
        #     last_index[x]=i
        # return False

nums=[1,2,3,1,2,3]
k =2
print(containDuplicate(nums,k))