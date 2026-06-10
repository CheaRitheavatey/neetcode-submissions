class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # abc
        # lecabee
        #   l
        #      r

        #      if length is the same return true

        # left move when we dont see it in s1 and r move everytime
        if len(s2) < len(s1): return False

        ss1 = [0] * 26
        ss2 = [0] * 26

        for i in range(len(s1)):
            ss1[ord(s1[i]) - ord('a')]+=1
            ss2[ord(s2[i]) - ord('a')]+=1

        if ss1 == ss2:
            return True
        
        l = 0
        ss = set()
        for r in range(len(s1), len(s2)):
            ss2[ord(s2[r]) - ord('a')]+= 1
            ss2[ord(s2[l]) - ord('a')]-= 1
            l+=1
            
            if ss1 == ss2:
                return True
        return False


        