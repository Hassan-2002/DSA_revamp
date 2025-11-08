#Given an integer array nums, rotate the array to the right by k steps, 
#where k is non-negative.
#Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4] 

#first idea was to use two pointers but found a better solution
#reverse the array entirely then we rotate two inversed smaller arrays at the kth index

def rotate(nums : list[int], k : int) -> None:
    print("Original nums ", nums)
    nums.reverse()
    print("reversed array entirely", nums)
    length = len(nums)
    k=k%length #incase k exceeds the lenght of the array, we reduce it to this
    nums[:k] = reversed(nums[:k])
    print("first half rotated", nums)

    nums[k:] = reversed(nums[k:])
    print("rotated nums", nums)
 
nums = [1,2,3,4,5,6,7]
rotate(nums, 1)
