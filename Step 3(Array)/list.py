# n = int(input())
# budget = int(input())
# arr = list(map(int, input().split()))

# best_sum = 0
# a = b = 0

# for i in range(n):
#     for j in range(i+1, n):
#         s = arr[i] + arr[j]
#         if s <= budget and s > best_sum:
#             best_sum = s
#             a = arr[i]
#             b = arr[j]

# print(a)
# print(b)

# A = [1,3,6,4,1,2]
A=[1,2,3]
# n = len(A)
# ans =0
# for i in range(n):
#     if i in A:
#         continue
#     else:
#         if i > 0:
#             print(i)
new_a=set(A)
i =1
while i in new_a:
    i+=1

print(i)

# Slow code with Time complexity of O(n^2) 
'''
B=[3,1,2,4,3]
unqiue_elements = set(B)
n = len(unqiue_elements)
min_val = float('inf')
sum1 = 0
sum2 =0

for p in range(1,n+1):
    part1 = B[:p]
    part2 = B[p:]
    sum1 = 0
    sum2 =0
    for i in part1:
        sum1 +=i
    for j in part2:
        sum2 += j
    
    min_val = min(min_val , abs(sum1 - sum2))

print(min_val)

'''

# Prefix_sum
B = [3 , 1 , 2 ,4 ,3]
total_sum = sum(B)
left_sum = 0
min_val = float('inf')
for i in range(len(B) - 1):
    left_sum += B[i]
    right = total_sum - left_sum

    diff = abs(left_sum-right)   

    if diff < min_val:
        min_val = diff

print(min_val)
