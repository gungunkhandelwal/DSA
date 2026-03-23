def sort_stack(stack):
    temp_stack = []
    i=0
    while stack:
        temp = stack.pop()
        i=i+1
        print(f"total {i}")

        while temp_stack and temp_stack[-1] > temp:
            print(f"If {temp_stack} and {temp} for this{stack}")
            stack.append(temp_stack.pop())
            print(f"Updated {stack}")

        temp_stack.append(temp)
        print(temp_stack)

    # while temp_stack:
    #     stack.append(temp_stack.pop())

    return temp_stack

A=[34,3,31,98,92,23]
print(sort_stack(A))