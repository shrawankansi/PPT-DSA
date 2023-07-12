def threeSumClosest(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    closestSum = float('inf')  

    for i in range(n - 2):  
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                return target  

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            else:
                right -= 1

    return closestSum
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)