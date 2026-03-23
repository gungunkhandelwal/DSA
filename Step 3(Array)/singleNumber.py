def singlenumber(nums):
        
        # Approach 1: Brute force time complexity O(n^2){becoz count also create loope inside array} and S.C O(1)
        # for num in nums:
        #     if nums.count(num) ==1:
        #         return num

        
        #Approach 2: Sorted Technique : T.c->O(nlogn) and space complexity -> O(1)
        # nums.sort()
        # i=0
        # while i< len(nums)-1:
        #     if nums[i] !=nums[i+1]:
        #         return nums[i]
        #     i+=2
        # return nums[-1]

        #Approach 3: Bitwise XOR : T.C-->O(n) and S.C --> O(1)
        res=0
        for num in nums:
            res ^=num
        return res

A=[2,2,1]
# A=[4,1,2,1,2]
print(singlenumber(A))
            