def func(nums):
    res = []
    for i in range(len(nums)):
        target = nums[i]
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
               count+=1
        res.append(count)
    return res

def func_optimized(nums):
    res = []
    nums_sorted = sorted(nums)
    nums_sorted_visited = {}
    for i in range(len(nums_sorted)):
        if nums_sorted[i] not in nums_sorted_visited:
            nums_sorted_visited[nums_sorted[i]] = i
    for i in range(len(nums)):
        res.append(nums_sorted_visited[nums[i]])
    return res
    
nums = [8,1,2,2,3]
print(func(nums))
print(func_optimized(nums))