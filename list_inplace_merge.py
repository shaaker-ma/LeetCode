"""
Given two sorted arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
nums1 has enough space (size m + n) to hold additional elements.

Input:
nums1 = [1,2,3,0,0,0], m = 3  
nums2 = [2,5,6], n = 3

Output:
[1,2,2,3,5,6]

"""

def sort1(l1, l2):
  nums_all = nums1 + nums2
  nums_all.sort()
  nums_out = nums_all[len(nums1)-len(nums2):]
  return nums_out

def sort2(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while(j>=0):
        if(i>=0 and nums1[i]>nums2[j]):
           nums1[k] = nums1[i]
           i = i-1
        else:
           nums1[k] = nums2[j]
           j = j-1 
        k = k-1
    return nums1

  

nums1 = [1,2,3,0,0,0]
nums2 = [1,2,8]
sorted_list = sort1(nums1, nums2)
sorted_list = sort2(nums1, 3, nums2, 3)
print(sorted_list)