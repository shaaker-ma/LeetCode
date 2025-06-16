"""
Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.
"""

def func(nums):
    visited_nums = set()
    for i in range(len(nums)):
        if nums[i] in visited_nums:
            return True
        visited_nums.add(nums[i])
    return False
