"""
"""

def func(nums):
    nums_set = set(nums)
    for i in range(len(nums)+1):
        if(i not in nums_set):
            return i
# Example usage:
nums = [0, 1, 2, 3, 5]
print(func(nums))  # Output: 4
# Time Complexity: O(n)
# Space Complexity: O(n), where n is the size of the input array.

def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
# Example usage:
nums = [0, 1, 2, 3, 5]
print(missingNumber(nums))  # Output: 4
# Time Complexity: O(n)
# Space Complexity: O(1), since we are using a constant amount of extra space.