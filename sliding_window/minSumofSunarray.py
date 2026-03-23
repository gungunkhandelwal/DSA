from math import inf

# def minimumSumSubarray(nums, l,r):
#         n=len(nums)
#         i,j=0,0
#         window_sum=0
#         min_sum=float(inf)
#         while j<n:
#             window_sum += nums[j]

#             while j-i+1 >r:
#                 window_sum -=nums[i]
#                 i+=1
            
#             if l<=j-i+1 <= r:
#                 if window_sum >0:
#                     min_sum=min(min_sum,window_sum)
            
#             j+=1
#         return min_sum if min_sum != float(inf) else -1
def minimumSumSubarray(nums, l,r):
        n=len(nums)
        min_sum=float(inf)
        for k in range(l,r+1):
            window_sum=sum(nums[:k])
            if window_sum >0:
                min_sum=min(min_sum,window_sum)
            for i in range(k,n):
                window_sum+=nums[i]-nums[i-k]
                if window_sum>0:
                    min_sum=min(min_sum,window_sum)

        return min_sum if min_sum != float(inf) else -1


A=[3,-2,1,4]
l=2
r=3
print(minimumSumSubarray(A,l,r))


# Time complexity O(n^2) and space complexity O(1)