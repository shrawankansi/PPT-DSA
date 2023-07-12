def nearestSmallerElements(a):
    stack = []
    result = []

    for num in a:
        while stack and stack[-1] >= num:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(num)

    return result



a = [1, 6, 2]

result = nearestSmallerElements(a)


for num in result:
    print(num, end=" ")
