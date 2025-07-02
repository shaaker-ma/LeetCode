def func(nums):
    max_num = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(current_sum+nums[i], nums[i])
        max_num = max(max_num, current_sum)
    return max_num