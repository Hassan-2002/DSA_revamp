# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i = 0
        zeroes = 0
        maxLen = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[i] == 0:
                    zeroes -= 1
                i += 1
            maxLen = max(maxLen, j - i + 1)
        return maxLen

nums = list(map(int, input().split(',')))
k = int(input())

s = Solution()
ans = s.longestOnes(nums, k)
print(ans)

