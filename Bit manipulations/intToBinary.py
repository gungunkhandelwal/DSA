
def intTobinary(n):
    # Time complexity -> O(log n) and space complexity -> O(log n)
    res=''
    while n > 0:
        if n%2 == 1:
            res += '1'
        else:
            res += '0'
        n = n//2
    return res[::-1]

n = 13
print(intTobinary(n))

def binaryToint(s):
    # Time complexity ->O(n) and space complexity ->O(1)
    n = len(s)
    p = 1
    num = 0
    for i in range(n-1,-1,-1):
        if s[i] == '1':
            num = num + p 
        p = p*2
    return num

s = '1101'
print(binaryToint(s))