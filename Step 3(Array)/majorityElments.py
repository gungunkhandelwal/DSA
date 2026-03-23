from collections import defaultdict


def majorityElements(nums):
    count=defaultdict(int)
    n=len(nums)
    for i in range(n):
        count[nums[i]]+=1
    for key,value in count.items():
        if value > n//2:
            return key

a=[2,2,1,1,1,2,2]
print(majorityElements(a))
b=[3,2,3]
print(majorityElements(b))

c=[1]
print(majorityElements(c))

d=[2,2]
print(majorityElements(d))


