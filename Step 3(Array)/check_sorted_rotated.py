# Brute Force

def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i] <arr[i-1]:
            return False
    return True

def check(num):
    n=len(num)
    for i in range (n):
        rotated=num[i:] + num[:i]
        print(num[i:])
        print(num[:i])
        print(rotated)
        if is_sorted(rotated):
            return True
    return False

A=[3,4,5,1,2]
print(check(A))
print('#################')
B=[2,1,4,5]
print(check(B))
# Time complexit - O(n^2) and space complexity :O(n)

# Approach 2 - sliding window
def check_rotated(nums):
    n=len(nums)
    count=0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            count +=1
            if count > 1:
                return False
    return True

A=[2,1,5,4]
print(check_rotated(A))

# Time complexit - O(n^2) and space complexity :O(1)

def func(x):
    x[1] = 'b'

a = {1:'a'}
func(a)
print(a)
