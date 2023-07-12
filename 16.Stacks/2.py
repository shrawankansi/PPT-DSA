def sortStack(stack):
    temp_stack = []

    while stack:
        temp = stack.pop()

        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())

        temp_stack.append(temp)

    sorted_stack = []

    while temp_stack:
        sorted_stack.append(temp_stack.pop())

    return sorted_stack


stack = [34, 3, 31, 98, 92, 23]

sorted_stack = sortStack(stack)


print(sorted_stack)
