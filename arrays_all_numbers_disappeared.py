def func(nums):
    res = []
    visited = set(nums)
    for i in range(1, len(nums)+1):
        if(i not in visited):
            res.append(i)
    return res