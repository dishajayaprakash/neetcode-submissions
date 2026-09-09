from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        sorted_values = sorted(
            freq_map.items(),
            key = lambda item: item[1],
            reverse = True
        )
        return [num for num, freq in sorted_values[:k]]