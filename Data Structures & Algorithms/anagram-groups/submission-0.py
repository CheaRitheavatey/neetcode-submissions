class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # break all the str
        store = {}
        res = []
        for i in range(len(strs)):
            x ="".join(sorted(strs[i]))
            # store it into a dict?
            if x not in store:
                store[x] = []
            store[x].append(strs[i])
        
        for i in store.values():
            res.append(i)
        # print(store)
        # print(res)
        return res

        