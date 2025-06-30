def func(nums):
    nums.sort()
    min_diff = nums[-1] - nums[0] # max diff
    res = []
    for i in range(len(nums)-1):
        min_diff = min(min_diff, nums[i+1]-nums[i])
    for i in range(len(nums)-1):
        if nums[i+1]-nums[i] == min_diff:
            res.append([nums[i], nums[i+1]])
    return res
        

nums = [4,2,1,3]
print(func(nums))

nums = [1,3,6,10,15]
print(func(nums))

nums = [3,8,-10,23,19,-4,-14,27]
print(func(nums))