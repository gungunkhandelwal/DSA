# optimal solution
arr=[2,4,12,42,21,32,1]
max_value=arr[0]
for i in arr:
    if max_value<i:
        max_value=i
print(f"The max value in arr {max_value}")

# Time complexity -O(n) and space complexity O(1)

# Brute force
def largestElement(nums):
    nums.sort()
    return nums[-1]

print(largestElement(arr))

# Time complexity O(nlogn)