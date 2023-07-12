def minScore(nums, k):
    min_val = min(nums)
    max_val = max(nums)
    
    if min_val + k >= max_val - k:
        return 0
    
    return max_val - k - (min_val + k)
