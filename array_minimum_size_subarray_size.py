def func(nums, target):
    left = 0
    min_len = len(nums)
    current_sum = 0
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right-left+1)
            current_sum -= nums[left]
            left +=1
    return min_len

nums = [2,3,1,2,4,3]
target = 7
print(func(nums, target))
