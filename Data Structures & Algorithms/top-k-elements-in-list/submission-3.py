class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        array = [[] for i in range(len(nums)+1)]

        for key,value in count.items():
            array[value].append(key)

        result = []
        for i in range(len(nums), 0, -1):
            for j in array[i]:
                result.append(j)
                if len(result) == k:
                    return result


        