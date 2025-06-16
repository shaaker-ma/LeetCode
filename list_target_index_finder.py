"""
Prompt:
Given a sorted array of integers and a target, return the first and last position of that target. If not found, return [-1, -1].

python
Copy
Edit
nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

"""

def target_idx_finder(nums, target):
    first_idx = -1
    last_idx = -1
    for i in range(len(nums)):
        if nums[i]==target:
            if first_idx == -1:
                first_idx = i
            last_idx = i
    return [first_idx, last_idx]


target = 7
nums = [5,7,7,8,8,10]
result = target_idx_finder(nums, target)
print(result) 
