class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # O U Z O D Y X A Z V
        # XYZ
        # len = 5
        # store both s and t
        if s == t: return t
        if len(t) > len(s): return ""

        store = {}
        store_t = {}
        # store = [""] * len(s)
        longest = float('inf')
        for i in range(len(t)):
            store_t[t[i]] = store_t.get(t[i],0) + 1
            # store_s[s[i]] = store_s.get(s[i],0) + 1
            # store[i] = s[i]

        # if store_s == store_t: return t
        l = 0
        need = len(store_t)
        have = 0
        result = [-1,-1]
        # ranger = (0,0)
        for r in range(len(s)):
            store[s[r]] = store.get(s[r],0) + 1
            # while all the element of t in store
            if s[r] in store_t and store[s[r]] == store_t[s[r]]:
                have += 1
            while have== need:
                if (r-l+1) < longest:
                    result = [l,r]
                    longest = r - l + 1
                # shrink window
                store[s[l]] -= 1
                if s[l] in store_t and store[s[l]] < store_t[s[l]]:
                    have -=1

                l+=1
        # if longest == float('inf'): return ""
        l,r = result
        return s[l:r+1] if longest != float('inf') else ""




        