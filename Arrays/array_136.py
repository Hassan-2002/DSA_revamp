# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.
from collections import Counter
def single(nums) -> int:
   num_count = Counter(nums)
   for i in num_count:
      if num_count[i] == 1:
        return i
   print(num_count)

nums = [1,1,2,2,3]
single(nums)