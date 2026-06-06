class Solution:
    def isPalindrome(self, s: str) -> bool:
        # trim s and ignore any symbol that is not relevant
        s = s.lower().replace(" ", "")
        
        special_char = "@_!#$%^&*()<>?/\|}{~:,-.[ ]'\"`"
        for i in special_char:
            s = s.replace(i, "")
        
        l ,r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
