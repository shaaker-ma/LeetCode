def func(nums):
    max_height = 0
    for i in range(1, len(nums)-1):
        left, right = i-1, i+1
        if(nums[i]>nums[left] and nums[i]>nums[right]):
            while left>0 and nums[left]>nums[left-1]:
                left -= 1
            while right<len(nums)-1 and nums[right]>nums[right+1]:
                right += 1
            max_height = max(max_height, right - left+1)
    return max_height 
    
nums = [2,1,4,7,3,2,5]
print(func(nums))

nums = [2,2,2]
print(func(nums))
