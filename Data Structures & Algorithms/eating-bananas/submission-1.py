class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles) # if koko can eat one pile in max(piles) then of course she can eat the rest as well
        while low <= high:
            k = (low + high) // 2 # current speed
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / k) # total time needed at this speed
            # If the total hours is within the allowed time h, try to find a smaller working speed by searching the lower half.
            if total_time <= h: 
                res = k
                high = k - 1
            # Speed is too slow, so search in the right half.
            else:
                low = k + 1
        return res
        