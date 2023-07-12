def sorted_squares(nums):
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] * nums[left])
            left += 1
        else:
            result.append(nums[right] * nums[right])
            right -= 1

    return result[::-1]
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)