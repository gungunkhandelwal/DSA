# It is correct but time execution is larger because in question ther are not asking for 32-bit signed interger
def isPalidrome1(x):
        INT_MIN,INT_MAX=-2**31,2**31-1
        negative=x<0
        original=x
        result=0
        x=abs(x)


        while x!=0:
            last_digit=x%10
            result=(result*10)+last_digit
            x//=10
        
        if negative:
            return False

        if x<INT_MIN or x>INT_MAX:
            return 0
        
        return original==result


def isPalidrome(x):
        if x<0:
            return False
        
        original=x #copy varuable because we are modifying x in futher step
        result=0
        while x!=0:
            last_digit=x%10
            result=(result*10)+last_digit
            x//=10
        
        return original == result
# Time complexity O(logn) its time excuetion is lower the above  but has same time complexity
     

x=-121
print(isPalidrome1(x))
print(isPalidrome(x))