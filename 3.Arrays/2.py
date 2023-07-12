def fourSum(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    result = []

    for i in range(n - 3):  # Iterate through the array
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]

                if currentSum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1

    return result
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)
