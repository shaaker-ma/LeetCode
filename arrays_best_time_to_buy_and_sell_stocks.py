def func(nums):
    left = 0
    max_profit = 0
    for i in range(1, len(nums)):
        if(nums[left]>nums[i]):
            left = i
        max_profit = max(max_profit, nums[i] - nums[left])
    return max_profit


nums = [7,1,5,3,6,4]
print(func(nums))

nums = [7,6,4,3,1]
print(func(nums))