from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Optimal solution(TWO POINTER) - Time complexity -O(N) and space complexity: O(1)
        '''
        left , right = 0 , len(height) -1
        leftMax , rightMax = 0 , 0
        water = 0
 
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                
                left +=1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -=1
        
        return water
    
        '''
        Better using STACK -> Time complexity:O(n) and space complexity - O(n)
        '''
        # stack=[]
        # water=0
        # n = len(height)

        # for i in range(n):
        #     while stack and height[i] > height[stack[-1]]:
        #         bottom = stack.pop()

        #         if not stack:
        #             break
                
        #         left = stack[-1]
        #         width = i - left - 1
        #         bounded = min(height[left], height[i]) -height[bottom]
        #         water += width * bounded
            
        #     stack.append(i)
        
        # return water

        '''
        Better using DP prefix/suffix Approach -> time complexity - O(n) and space complexity - O(n)
        '''
        # n=len(height)
        # maxLeft=[0]*n
        # maxRight=[0]*n
        # maxLeft[0] = height[0]
        # maxRight[n-1] = height[n-1]
        # water=[0]*n
        # sum_area=0

        # for i in range(1,n):
        #     maxLeft[i] = max(maxLeft[i-1],height[i])
        
        # for j in range(n-2, -1, -1):
        #     maxRight[j] = max(maxRight[j+1],height[j])
        
        # for i in range(n):
        #     water[i] = min(maxLeft[i],maxRight[i]) - height[i]
        
        # for i in range(n):
        #     sum_area += water[i]
        
        # return sum_area

A=[4,2,0,3,2,5]
s=Solution()
print(s.trap(A))