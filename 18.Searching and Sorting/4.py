def radixSort(nums):
    if not nums or len(nums) < 2:
        return nums

    # Find the maximum element in the array
    max_num = max(nums)

    # Perform radix sort
    exp = 1
    while max_num // exp > 0:
        countingSort(nums, exp)
        exp *= 10

def countingSort(nums, exp):
    n = len(nums)
    count = [0] * 10
    output = [0] * n

    
    for i in range(n):
        index = (nums[i] // exp) % 10
        count[index] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]

    
    for i in range(n - 1, -1, -1):
        index = (nums[i] // exp) % 10
        output[count[index] - 1] = nums[i]
        count[index] -= 1

    
    for i in range(n):
        nums[i] = output[i]

def maximumGap(nums):
    if not nums or len(nums) < 2:
        return 0


    radixSort(nums)

    
    max_diff = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        max_diff = max(max_diff, diff)

    return max_diff



nums = [3, 6, 9, 1]

max_diff = maximumGap(nums)


print(max_diff)
