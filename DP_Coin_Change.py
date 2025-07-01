def func(nums, amount):
    amounts_sol = [float('inf')]*(amount+1)
    amounts_sol[0] = 0
    
    for i in range(len(amounts_sol)):
        for num in nums:
            if(i-num >= 0):
                amounts_sol[i] = min(amounts_sol[i], amounts_sol[i-num]+1)
    if(amounts_sol[amount] == float('inf')):
        return -1
    return amounts_sol[amount]

nums = [1,2,5]
amount = 11
print(func(nums, amount))
nums = [2]
amount = 3
print(func(nums, amount))
nums = [1]
amount = 0
print(func(nums, amount))