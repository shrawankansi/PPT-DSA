def deleteMiddleElement(stack):
    size = len(stack)

    
    middle_index = (size // 2) + (1 if size % 2 == 1 else 0)

    
    for _ in range(middle_index - 1):
        stack.pop()

    return stack



stack = [1, 2, 3, 4, 5]

modified_stack = deleteMiddleElement(stack)


print(modified_stack)
