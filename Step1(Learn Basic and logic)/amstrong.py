def isAmstrongNumber(n:int)->bool:
    original=n
    x=len(str(n))
    ams_num=0
    while n!=0:
        digit=n%10
        ams_num=(digit**x)+ams_num
        n//=10
    
    return original == ams_num

n=153
print(isAmstrongNumber(n))

if isAmstrongNumber(n):
    print(f"{n} is an amstrong number")
else:
    print(f"{n} is not an amstrong number")
    