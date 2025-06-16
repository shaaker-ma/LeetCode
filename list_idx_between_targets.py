"""
Prompt:
Given a sorted array arr, an integer k, and a target x, return the k closest elements to x.

Input:

python
Copy
Edit
arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
"""

def func(arr, target, x):
    first_idx, second_idx = 0, len(arr)-1
    while(first_idx <= second_idx):
        current_middle = (first_idx + second_idx) // 2
        if(arr[current_middle] < target):
            first_idx = current_middle+1
        elif(target < arr[current_middle]):
            second_idx = current_middle-1
        elif(target == arr[current_middle]):
            return arr[current_middle-x:current_middle]
    

arr = [1,2,3,4,5]
k = 4
x = 3
res = func(arr, k, x)
print(res)