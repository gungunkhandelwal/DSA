# def maxRamp(nums):
#             def FindSmallestLeft(nums):
#                 result=[]
#                 stack=[]

#                 for i in range(len(nums)):
#                     while len(stack) > 0 and stack[-1][0] >=nums[i]:
#                         stack.pop()
#                     if not stack:
#                         result.append(-1)
#                     else:
#                         result.append(stack[-1][1])
#                     stack.append((nums[i],i))
#                 return result
        
#             def FindSmallestRight(nums):
#                 result=[]
#                 stack=[]

#                 for i in range(len(nums)-1,-1,-1):
#                     while len(stack) >0 and stack[-1][0] >=nums[i]:
#                         stack.pop()
#                     if not stack:
#                         result.append(-1)
#                     else:
#                         result.append(stack[-1][1])
                    
#                     stack.append((nums[i],i))
#                 return result[::-1]
            
#             right=FindSmallestLeft(nums)
#             print(right)
#             left=FindSmallestRight(nums)
#             print(left)

#             width=[]
#             for i in range(len(nums)):
#                 width.append(right[i]-left[i]-1)
#             print(width)
            
#             return max(width)

# A=[6,0,8,2,1,5]
# B=[0,1]
# print(maxRamp(A))
# print(maxRamp(B))

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        print(stack)

        max_width = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())
                
        return max_width

s=Solution()
print(s.maxWidthRamp([6,0,8,2,1,6]))

