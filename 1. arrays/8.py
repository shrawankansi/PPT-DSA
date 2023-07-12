def findErrorNums(nums):
    n = len(nums)
    numSet = set()
    totalSum = (n * (n + 1)) // 2
    arraySum = 0
    duplicateNum = 0

    for num in nums:
        arraySum += num
        if num in numSet:
            duplicateNum = num
        numSet.add(num)

    missingNum = totalSum - arraySum

    return [duplicateNum, missingNum]


nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)
