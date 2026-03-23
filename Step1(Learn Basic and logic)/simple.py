def printNto1(i,n):
    if i<1:
        return
    print(i)
    printNto1(i-1,n)

printNto1(4,4)

print('############')

def print1toN(i,n):
    if i>n:
        return
    print(i)
    print1toN(i+1,n)

print1toN(1,9)

print('#################')
def printNname(s,i,n):
    if i>n:
        return
    print(s)
    printNname(s,i+1,n)

printNname("Gungun",1,10)