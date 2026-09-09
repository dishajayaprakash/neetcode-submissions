class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            k = (low + high) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / k)
            if total_time <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        return res
        