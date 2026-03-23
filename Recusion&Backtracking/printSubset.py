def printSubset(arr , ans , i):
    n = len(arr)
    if i == n:
        print(ans)
        return
    ans.append(arr[i])
    printSubset(arr , ans , i+1)
    ans.pop()
    printSubset(arr , ans , i +1)


arr = [1,2,3]
ans = []
i = 0
print(printSubset(arr,ans,i))
