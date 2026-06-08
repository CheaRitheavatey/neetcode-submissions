class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "z xyzxyz"
        #    l  r
        # string = z
        l = 0
        result = 0
        long = set()
        for r in range(len(s)):
            while s[r] in long:
                long.remove(s[l])
                l+=1
            long.add(s[r])
            result = max(result, r-l+1)
        return result
           
        