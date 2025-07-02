class NumArray:
    def __init__(self, nums):
        self.all_nums = nums 
        
    def sumRange(self, left, right):
        count = 0
        for i in range(left, right+1):
            count += self.all_nums[i]
        return count
        
class NumArray:
    def __init__(self, nums):
        self.sums = [0]
        for i in range(len(nums)):
            self.sums.append(nums[i] + self.sums[-1])
        
    def sumRange(self, left, right):
        return self.sums[right+1] - self.sums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # Output: 1
print(obj.sumRange(2, 5))  # Output: -1
print(obj.sumRange(0, 5))  # Output: -3