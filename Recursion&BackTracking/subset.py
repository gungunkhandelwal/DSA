def subset(nums):
    res = []

    def backtrack(state , current):
        res.append(current[:])

        for i in range(state , len(nums)):
            current.append(nums[i])
            backtrack(i+1 , current)
            current.pop()

    backtrack(0 , [])
    return res

nums = [1,2,3]
print(subset(nums))


