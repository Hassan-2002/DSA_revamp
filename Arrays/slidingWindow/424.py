
# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        if len(s)==1:
            return 1
        for i in range(len(s)-1):
            changes = 0
            j=i+1
            while changes<k and j<len(s):
                if s[j]!=s[i]:
                    changes+=1
                    
                    j+=1
                else:
                    j+=1
                print(i,j)    
         
            maxlen = max(maxlen,  j-i)
        return maxlen   

s = Solution()
arr = str(input())
k = int(input())

ans = s.characterReplacement(arr, k)
print(ans)


        