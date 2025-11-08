# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
from collections import Counter
def freq(nums, k):
    count = Counter(nums)
    print(count)
    count_list = list(count.values())
    print(count_list)
    count_list.sort(reverse = True)
    print(count_list)
    answer = []
    for i in range(k):
        answer.append(count[count_list[i]])
    return answer 
nums = [1,1,1]
k = 1
answer = freq(nums, k)
print(answer)
         