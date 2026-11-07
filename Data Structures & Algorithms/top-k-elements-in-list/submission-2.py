class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            bucket[value].append(key)
       
        result = []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result
