# Brute force
def sumofn(n):
    sum_num=0
    for i in range(1,n+1):
        sum_num +=i
    return sum_num

print(sumofn(123))

# Time complexity O(n)and space complexity is O(1 )

# Recursion algo
def recursivesum(i,n,sum_num=0):
    if i>n:
        print(sum_num)
        return
    recursivesum(i+1,n,sum_num+i)


recursivesum(1,7)

# Time complexity O(n) and space complexity O(n) <-- recursive call stack