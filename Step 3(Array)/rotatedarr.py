class Solution:
    def rotate(self, nums,k) -> None:
        '''Approach 1: extra array T.C -->O(n) && S.C-->O(N)'''
        # n=len(nums)
        # k=k%n
        # rotated=[0]*n
        # for i in range(n):
        #     rotated[(i+k)%n]=nums[i]

        # nums[:]=rotated

        '''Approach 2: slicing T.C -->O(n) && S.C-->O(N)'''
        # n=len(nums)
        # k=k%n
        # nums[:]=nums[-k:]+nums[:-k]
        
        '''Approach 3: Reverse method T.C -->O(n) && S.C-->O(1)'''

        n=len(nums)
        k=k%n
        l,r=0,n-1
        self.reverse_arr(nums,l,r)
        l,r=0,k-1
        self.reverse_arr(nums,l,r)
        l,r=k,n-1
        self.reverse_arr(nums,l,r)

        return nums

    def reverse_arr(self,nums,l,r):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1

A1=[1,2,3,4,5,6,7]
k1=3
output1=Solution()
print(output1.rotate(A1,k1))
A2=[-1,-100,3,99]
k2=2
output2=Solution()
print(output2.rotate(A2,k2))