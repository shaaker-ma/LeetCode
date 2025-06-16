
def func(nums): # O(nlogn) time and O(1) Space
    for i in range(len(nums)):
        nums[i] = nums[i]*nums[i]
    nums.sort()
    return nums

def func_optimized(nums): # O(n) time and O(n) Space
    left, right = 0, len(nums)-1
    res = []
    while right >= left:
        right_powered = nums[right]**2
        left_powered = nums[left]**2
        if(right_powered>left_powered):
            res.append(right_powered)
            right -=1
        else:
            res.append(left_powered)
            left +=1
    res = res[::-1]
    return res

nums = [-4,-1,0,3,10]
print(func(nums))
nums = [-4,-1,0,3,10]
print(func_optimized(nums))