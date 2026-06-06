class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        result = []
        for i in nums:
            store[i] = store.get(i,0) + 1
        # print(store)

        store = dict(sorted(store.items(), key=lambda item: item[1],reverse=True))
        # print(store)

        result.extend(list(store.keys())[:k])
        # print(result)
        return result
        
            







        