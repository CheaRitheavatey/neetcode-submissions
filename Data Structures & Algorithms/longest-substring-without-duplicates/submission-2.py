class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        re = set()

        for r in range(len(s)):
            while s[r] in re:
                re.remove(s[l])
                l+=1
            re.add(s[r])
            longest = max(longest, r-l+1)
        return longest

        
        