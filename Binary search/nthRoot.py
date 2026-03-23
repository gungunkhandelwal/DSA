def nthRoot(n,m):
    left , right = 0,m
    while left <= right:
        mid = left + (right-left)//2

        if (mid **n) == m:
            return mid
        elif (mid**n)<m:
            left = mid +1
        else:
            right = mid -1
    return -1

n=3
m=27
print(nthRoot(n,m))

n1=4
m1=69
print(nthRoot(n1,m1))