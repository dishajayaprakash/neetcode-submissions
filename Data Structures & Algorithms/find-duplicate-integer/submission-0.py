class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n-1
        # If all numbers from 1 to mid appeared at most once, then the count of numbers <= mid should be <= mid
        while low < high:
            mid = low + (high-low) // 2
            # Count how many numbers in the array are <= mid 
            lessorequal = sum(1 for num in nums if num <= mid)
            if lessorequal <= mid: # if the count is lesser than mid, it lies in [mid + 1, high], so set low = mid + 1
                low = mid + 1
            else: # If the count is greater than mid, the duplicate lies in [low, mid], so set high = mid
                high = mid
        return low        