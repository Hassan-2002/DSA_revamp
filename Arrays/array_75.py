# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function
# we could just brute force by counting the number of 0s 1s and 2s 

#brute force solution
from collections import Counter
def brute(nums):
    count = Counter(nums)
    num = []*len(nums)
    for i in range(len(num)):
        if i < count[0]:
            num[i]==0
        elif i<count[0]+count[1]:
            num[i]==1
        else:
            num[i]==2
    return num

nums = [2,0,2,1,1,0]
num = brute(nums)
print(num)
#optimal approach using 3 pointers
i,j,k = 0,0,len(nums)-1
while j<=k:
    if nums[j]==0:
        nums[i], nums[j] = nums[j],nums[i]
        i+=1
        j+=1
    elif nums[j] == 1:
         j+=1
    else:
        nums[k], nums[j] = nums[j], nums[k]
        j+=1
        k+-1
print(nums)