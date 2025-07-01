def func(nums):
    visited = {}
    for i in range(len(nums)):
        if nums[i] not in visited:
            visited[nums[i]] = 1
        else:
            visited[nums[i]] += 1
    print(visited.keys())
    print(visited.values())
    return list(visited.keys())[list(visited.values()).index(1)]

def func(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR eventually cancels out duplicate numbers
        print(f"nums: {num}, result: {result}")
    return result

nums = [2,2,1]
print(func(nums))
nums = [4,1,2,1,2]
print(func(nums))
nums = [1]
print(func(nums))
