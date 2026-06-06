class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # storing s  and storing t
        # if both s and t the same return true

        ss = []
        tt = []

        for i in s:
            ss.append(i)
        for i in t:
            tt.append(i)

        return sorted(ss) == sorted(tt)
        
        


        