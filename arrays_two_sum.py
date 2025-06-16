def func(nums, target):
    visited = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in visited:
            return [visited[diff], i]
        else:
            visited[nums[i]] = i 
        
    

nums = [2,7,11,15]
target = 9
print(func(nums, target))
print(func([2,3,4], 6))