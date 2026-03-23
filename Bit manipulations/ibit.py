def ibit(n,idx):
    # Brute force

    # res = ''
    # while n >0:
    #     if n %2 == 1:
    #         res += '1'
    #     else:
    #         res += '0'
    #     n = n//2
    
    # temp = res[::-1]

    # if idx < 0 or idx >= len(temp):
    #     return False

    # return temp[-(idx + 1)] == '1'

    ''' Time and space compllexity is O(1)'''
    # Using left shift
    # if (n & (1 << idx)) != 0:
    #     print((n & (1 << idx)))
    #     print(((1 << idx)))

    #     return True
    # else:
    #     return False

    # Using Right shift
    if ((n>>idx) & 1) != 0:
        print((n & (1 << idx)))
        print(((1 << idx)))

        return True
    else:
        print(1>>idx)
        return False

print(ibit(13,1))

def setI(n,i):
    if (n | (1 << i)) != 0:
        print((n | (1 << i)))
        return True
    else:
        print((n | (1 << i)))
        return False

print(setI(13 , 1))