def func(nums):
    left = right = 0
    max_profit = 0
    for right in range(len(nums)):
        if(nums[right]<nums[left]):
            left=right
        max_profit = max(max_profit, nums[right]-nums[left])
    return max_profit

nums = [7,1,5,3,6,4]
print(func(nums))

nums = [7,6,4,3,1]
print(func(nums))