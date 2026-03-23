from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

nums=[-2,0,3,-5,2,-1]
left=0
right=2
l1,r1=2,5
obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
param_2=obj.sumRange(l1,r1)
print(param_1)
print(param_2)
