def find_maximum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_maximum(arr[1:]))


arr = [1, 4, 3, -5, -4, 8, 6]
result = find_maximum(arr)
print(result)  # Output: 8

arr = [1, 4, 45, 6, 10, -8]
result = find_maximum(arr)
print(result)  # Output: 45
