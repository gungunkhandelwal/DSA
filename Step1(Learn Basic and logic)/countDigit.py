def countDigit(n):
    count=0
    while n>0:
        last_digit=n%10
        count +=1
        n //=10
    return count

n=int(input())
print(countDigit(n))

#Time complexity O(logn) and space complexit O(1)