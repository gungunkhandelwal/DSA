def union_arr(num1,num2):
    union_list=sorted(set(num1).union(num2))
    return union_list

            

num1=[1, 2, 3, 4, 5]
num2=[1, 2, 7]
print(union_arr(num1,num2))