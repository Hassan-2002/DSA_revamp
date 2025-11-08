# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# Input Format
# The first line contains an integer n the size of the nums array.

# The second line n elements of the array nums.

# Output Format
# Return true if it's possible to make a non-decreasing array, else return false.
def modify(arr : list) -> bool:
    numChanges = 0
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            if numChanges == 1:
                return False
            numChanges+=1
            if i==0 or arr[i-1] <= arr[i+1]:
                arr[i]=arr[i+1]
            else:
                arr[i+1]=arr[i]
    return True
test_cases = [
    ([1, 2, 3, 4, 5], True),  
    ([4, 2, 3], True),  
    ([1, 4, 2, 3], True),  # ✅ FIXED
    ([1, 2, 3, 7, 5], True),
    ([3, 4, 2, 1], False),
    ([5, 7, 1, 8], True),
    ([10], True),
    ([2, 1], True),
    ([1, 2, 2, 1], True),
    ([5, 4, 3, 2, 1], False),
    ([1, 5, 3, 4], True),
    ([2, 2, 2, 2], True),
    ([], True),
    ([10**5, 10**5, 10**5], True),
]

for nums, expected in test_cases:
    result = modify(nums)
    print(f"Input: {nums} | Output: {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")
