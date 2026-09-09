from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for num, count in freq_map.items():
            bucket[count].append(num)
        res = []
        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                res.append(num)
            if len(res) == k:
                return res