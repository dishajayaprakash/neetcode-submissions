class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in complement:
                return [complement[needed], i]
            complement[num] = i
        
        