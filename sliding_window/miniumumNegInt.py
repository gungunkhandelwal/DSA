def MinimumNegInt(arr,k):
    n=len(arr)
    i,j=0,0
    negative_arr=[]
    min_value=0
    while j<n:
        if(j-i+1 <k):
            j+=1
        elif (j-i+1 ==k):
            min_value=min(arr[i:j+1])
            if min_value <=0:
                negative_arr.append(min_value)
                min_value=0
            else:
                negative_arr.append(0)
            i+=1
            j+=1
    return negative_arr

arr=[-8, 2, 3, -6, 10]
k=2
print(MinimumNegInt(arr,k))