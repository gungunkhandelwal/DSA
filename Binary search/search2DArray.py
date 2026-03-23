def search2DArray(nums , target):
    rows = len(nums)
    cols = len(nums[0]) #for top-right corner
    i =0
    j = cols -1
    while i < rows and j >=0:
        if nums[i][j] == target:
            return i,j
        elif (nums[i][j] > target):
            j-=1
        else:
            i+=1
    return -1

arr= [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
target=29
print(search2DArray(arr,target))