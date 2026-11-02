class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = [0] * 26 
        arr_t = [0] * 26 

        for i in s:
            arr_s[ord(i)- ord('a')] += 1
        
        for i in t:
            arr_t[ord(i) - ord('a')] += 1
        return arr_s == arr_t