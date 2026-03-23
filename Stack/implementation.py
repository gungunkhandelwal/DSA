stack1=[1,2,4,3,5]
stack2=[]

while stack1:
    temp=stack1.pop()
    if temp and temp %2 ==0:
       stack2.append(temp)

print(stack2)


def reverseString(s):
    stack=[]
    for char in s:
        stack.append(char)
    reverse_str=''
    while stack:
        reverse_str+=stack.pop()
    return reverse_str

print(reverseString('gungun'))


def validPatheneses(s):
    mapping_dict={')':'(','}':'{',']':'['}
    stack=[]
    for char in s:
        if char in mapping_dict.values():
            stack.append(char)
        elif char in mapping_dict.keys():
            if not stack or mapping_dict[char]!= stack.pop():
                return False
    return not stack

s="()"
print(validPatheneses(s))
        
