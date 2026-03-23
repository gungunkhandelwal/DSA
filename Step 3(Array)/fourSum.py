def fourSum(nums,target):
        
        '''
        Better approch: time complexity->O(n^3) and space complexity -> O(n)
        '''
        res=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                hash_map=set()
                for k in range(j+1,n):
                    l=target-(nums[i]+nums[j]+nums[k])
                    if l in hash_map:
                        quadruplets=tuple(sorted([nums[i],nums[j],nums[k],l]))
                        res.add(quadruplets)
                    hash_map.add(nums[k])
        return [list(t) for t in res]

        '''
        Optimal Approach:  Time complexity->O(n^3) and space complexity->O(1) 
        '''

        # nums.sort()
        # n=len(nums)
        # res=[]
        # for i in range(n):
        #     if i!=0 and nums[i]==nums[i-1]:
        #         continue
        #     for j in range(i+1,n):
        #         if j!=i+1 and nums[j] ==nums[j-1]:
        #             continue
                
        #         k=j+1
        #         l=n-1
        #         while k<l:
        #             total_sum=nums[i]+nums[j]+nums[k]+nums[l]
        #             if total_sum < target:
        #                 k+=1
        #             elif total_sum > target:
        #                 l-=1
        #             else:
        #                 temp=[nums[i],nums[j],nums[k],nums[l]]
        #                 res.append(temp)
        #                 k+=1
        #                 l-=1
        #                 while k<l and nums[k]==nums[k-1]:
        #                     k+=1
        #                 while k<l and nums[l]==nums[l+1]:
        #                     l-=1
        # return res
        
        '''
        Brute Force : Time complexity->O(n^4) and space complexity->O(n)
        '''
        # res=set()
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             for l in range(k+1,n):
        #                 if (nums[i]+nums[j]+nums[k]+nums[l])==target:
        #                     quadruplets=tuple(sorted([nums[i],nums[j],nums[k],nums[l]]))
        #                     res.add(quadruplets)
        # return [list(t) for t in res]

nums =[1,0,-1,0,-2,2]
target=0
print(fourSum(nums,target))