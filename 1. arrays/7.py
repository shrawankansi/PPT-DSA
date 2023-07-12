def moveZeroes(nums):
    left = 0  

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1

    
    for i in range(left, len(nums)):
        nums[i] = 0


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
