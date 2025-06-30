def func(nums):
    time = 0
    current_state = nums[0]
    for i in range(len(nums)):
        if i == len(nums)-1:
            return time
        current_state = nums[i]
        next_state = nums[i+1]
        x_diff = abs(current_state[0] - next_state[0])
        y_diff = abs(current_state[1] - next_state[1])
        time = time + max(x_diff, y_diff)
    return time

nums = [[1,1], [3,4], [-1,0]]
print(func(nums))
nums = [[3,2],[-2,2]]
print(func(nums))

