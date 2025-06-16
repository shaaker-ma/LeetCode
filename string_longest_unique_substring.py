"""
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3  # "abc"
"""

def func(s):
    visited = set()
    max_total = 0
    left = 0
    for right in range(len(s)):
        while s[right] in visited:
            visited.remove(s[left])
            left = left+1
        visited.add(s[right])
        max_total = max(max_total, right-left+1)
    return max_total

s = "abcabcbb"
print(func(s))

# Trick: Sliding Winfow
# Time Complexity: O(n)
# Space Complexity: O(min(n, m)), where n is the size of the string and m is the size of the character set.