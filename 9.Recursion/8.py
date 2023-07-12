def product_of_array(arr):
    product = 1
    for num in arr:
        product *= num
    return product


arr = [1, 2, 3, 4, 5]
result = product_of_array(arr)
print(result)  # Output: 120

arr = [1, 6, 3]
result = product_of_array(arr)
print(result)  # Output: 18
