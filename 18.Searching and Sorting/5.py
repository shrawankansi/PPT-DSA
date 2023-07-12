def containsDuplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)

    return False


nums = [1, 2, 3, 1]

contains_duplicates = containsDuplicate(nums)


print(contains_duplicates)
