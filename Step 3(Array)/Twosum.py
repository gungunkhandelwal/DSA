def twoSum(nums, target):
        output=[]
        n=len(nums)
        for i in range(n):
            for j in range(1,n):
                if i == j:
                    break
                sumation=nums[i] +nums[j]
                if sumation == target:
                    output.extend([i,j])
        return output

output=[3,2,4]
target=6
print(twoSum(output,target))
# Time complexity -o(n^2) and space complexity- O(n^2)


# Better
def twoSums(nums, target):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]+nums[j]) == target:
                    return [i,j]
        return []

output=[3,3]
target=6
print(twoSums(output,target))
# # Time complexity -o(n^2) and space complexity- O(1)

# more better approach use Hash map

    