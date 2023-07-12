def find_max_length(nums):
    max_length = 0
    prefix_sums = {0: -1}
    running_sum = 0

    for i, num in enumerate(nums):
        running_sum += -1 if num == 0 else 1

        if running_sum == 0:
            max_length = max(max_length, i + 1)
        elif running_sum in prefix_sums:
            max_length = max(max_length, i - prefix_sums[running_sum])

        if running_sum not in prefix_sums:
            prefix_sums[running_sum] = i

    return max_length
nums = [0, 1]
result = find_max_length(nums)
print(result) 