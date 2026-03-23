from math import sqrt


def threeSum(nums):
        '''
        Optimal approch - Time complexity ->O(n^2) and space complexity ->O(1)
        '''
        result=[]
        nums.sort()
        n=len(nums)

        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum <0:
                    j+=1
                elif total_sum > 0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    result.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return result

        '''
        Better apprach - Time complexity ->O(n^2) and space complexity ->O(n)
        '''
        # n=len(nums)
        # result=set()
        # for i in range(n):
        #     hash_map=set()
        #     for j in range(i+1,n):
        #         k=-(nums[i]+nums[j])
        #         if k in hash_map:
        #             triplet=tuple(sorted([nums[i],nums[j],k]))
        #             result.add(triplet)
        #         hash_map.add(nums[j])
        # return [list(t) for t in result]
        
        '''
        Brute force with Time complexity-> O(n^3) and space complexity->O(n)
        '''
        # n=len(nums)
        # result=set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if (i!=j and i!=k and j!=k)and (nums[i]+nums[j]+nums[k] == 0):
        #                 triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 result.add(triplet)
        # return [list(t) for t in result]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))