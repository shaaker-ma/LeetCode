def func(nums, k):
    for i in range(len(nums)):
        right = i+1
        while abs(right - i) <= k and right< len(nums):
            if(nums[right] == nums[i]):
                return True
            right += 1  
    return False
    
def func_optimized(nums, k):
    visited = set()
    for i in range(len(nums)):
        if nums[i] in visited:
            return True
        visited.add(nums[i])
        if len(visited)>k:
            visited.remove(nums[i-k])
    return False

nums = [1,2,3,1]
k = 3
print(func_optimized(nums, k))

nums = [1,0,1,1]
k = 1
print(func_optimized(nums,k))

nums = [1,2,3,1,2,3]
k = 2
print(func_optimized(nums,k))



