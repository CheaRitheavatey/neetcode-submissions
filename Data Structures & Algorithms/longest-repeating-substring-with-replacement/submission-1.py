class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l = 0
        # longest = 0 
        # count = [0] * 26
        # for r in range(len(s)):
        #     count[ord(s[r]) - 65] += 1
        #     while (r - l + 1) - max(count) > k :
        #         count[ord(s[l]) -65] -= 1
        #         l+= 1
        #     longest = max(longest, (r-l+1))
        # return longest
        # # AAABABB
        # # for i in range: ber s[i] doch knea continue -> add jol set 
        # # ber a new char we never see yg trov covert
        # # max()
        
        l = 0
        store = [0] * 26
        longest = 0
        # X YYX
        # [0,0,...,1,2,0]
        for r in range(len(s)):
            store[ord(s[r]) - ord('A')]+= 1
            while (r - l + 1) - max(store) > k:
                store[ord(s[l]) - ord('A')] -= 1
                l+=1
            longest = max(longest, (r-l+1))
        return longest
            
        