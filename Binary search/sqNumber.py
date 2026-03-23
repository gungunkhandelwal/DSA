def sqNumber(n):
    left , right = 0 , n
    res=-1
    while left <= right:
        mid = left +(right - left)//2

        if mid * mid == n:
            return mid
        elif  mid * mid < n:
            res = mid
            left = mid + 1
        else:
            right = mid -1

    return res

n=28
print(sqNumber(n))
        