def twoSum(nums, target):
    complement_map = {}  
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in complement_map:
            return [complement_map[complement], i]
        
        complement_map[num] = i
    
    return []


nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)