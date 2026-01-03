class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        maxLen = 0
        hashset = set()
        for j in range(len(s)):
            if s[j] not in hashset:
                hashset.add(s[j])
                print(hashset)
            else:
                while s[j] in hashset and i<j:
                    hashset.remove(s[i])
                    i+=1
                  
            maxLen = max(maxLen, j - i + 1)
        return maxLen        


cll = Solution()
s = input()
ans = cll.lengthOfLongestSubstring(s)
print(cll)