arr=[1,2,3,12,34]
reverse_array1=[]
for i in range((len(arr)-1),-1,-1):
    reverse_array1.append(arr[i])
print(reverse_array1)
# time complexity O(n)

# two pointer
def reverse_array(arr,start,end):
    if start >=end:
        return
    arr[start],arr[end]=arr[end],arr[start]
    reverse_array(arr,start+1,end-1)

arr=[1,36,3,6,3,27,5,4]
reverse_array(arr,0,len(arr)-1)
print(arr)

# Time complexity O(n) and space complexity O(n)

print(16**0.5)