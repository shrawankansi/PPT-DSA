def reverseString(S):
    stack = []

    
    for char in S:
        stack.append(char)

    result = ""

    
    while stack:
        result += stack.pop()

    return result


S = "GeeksforGeeks"

reversed_string = reverseString(S)


print(reversed_string)
