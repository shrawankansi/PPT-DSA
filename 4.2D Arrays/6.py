def sorted_squares(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()

    return result
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result) 