def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

print(swap(5,6))

def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a =  a ^ b
    return a,b

print(swap1(5,6))