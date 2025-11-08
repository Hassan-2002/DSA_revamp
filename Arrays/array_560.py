#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def findsum( nums :list[int], k: int) -> int:
    count = total = 0
    hashmap = {0:1}
    for i in nums:
        total +=i
        if total - k in hashmap:
            count+=hashmap[total-k]
        hashmap[total] = 1 + hashmap.get(total, 0)

    return count
answer = findsum([1,2,3],3)
print(answer)