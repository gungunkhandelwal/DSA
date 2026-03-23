def gcd(n1,n2):
    if n2 ==0:
        return abs(n1)
    else:
        return gcd(n2,n1%n2)

n1,n2=4,6
print(gcd(n1,n2))


# simple way learning curve

n3=int(input())
n4=int(input())
gcd_num=1
for i in range(1,min(n3,n4)+1):
    if ((n3%i==0) and (n4%i==0)):
        gcd_num=i
print(gcd_num)

# Time complexity of O(n)
