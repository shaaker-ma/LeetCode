def func(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate i
        
        left, right = i + 1, len(nums) - 1
        while left<right:
            computed_sum = nums[left] + nums[i] + nums[right]
            if(computed_sum>0):
                right -= 1
            elif(computed_sum<0):
                left += 1
            else:
                current_result = [nums[left], nums[i], nums[right]]
                res.append(current_result)
                right -= 1
                left += 1
                while left<right and nums[left] == nums[left+1]:
                    left +=1
                while left<right and nums[right] == nums[right-1]:
                    right -=1
                
                
    return res
    
nums = [-1,0,1,2,-1,-4]
print(func(nums))

nums = [0,1,1]
print(func(nums))

nums = [0,0,0]
print(func(nums))