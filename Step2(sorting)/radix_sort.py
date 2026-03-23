def counting_sort_for_radix(arr,exp):
    n=len(arr)
    output=[0]*n
    count=[0]*10

    for i in arr:
        index=(i//exp)%10
        print(f'when {exp},{i}, {index}')
        count[index]+=1
        print(f'when {exp},{i}, {count}')
    
    for i in range(1,10):
        count[i] +=count[i-1]
        print(f"{exp},{i} -->{count[i]}")

    i=n-1
    while i>=0:
        index=(arr[i]//exp)%10
        output[count[index]-1]=arr[i]
        print(f'when {exp},{i}, {output[count[index]-1]}')
        count[index] -=1
        i -=1
    
    for i in range(n):
        arr[i]=output[i]
        print(f'output -->{output[i]}')
    

def radix_sort(arr):
    max_num=max(arr)
    exp=1
    while (max_num//exp) >0:
        counting_sort_for_radix(arr,exp)
        exp *=10

A = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(A)
print(A)


# Time complexity -O(n*k)
# space complexity -O(n)
