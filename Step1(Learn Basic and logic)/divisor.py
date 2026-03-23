n=int(input())
div_list=[]
for i in range(1,n+1):
    if n%i==0:
        div_list.append(i)

print(div_list)
# Time complexity O(n)
