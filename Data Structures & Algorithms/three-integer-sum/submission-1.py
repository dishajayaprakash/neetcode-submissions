class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for first in range(len(nums)):
            # duplicate starting point check
            if first > 0 and nums[first] == nums[first-1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                target = nums[first] + nums[second] + nums[third]
                if target == 0: # valid triplet found
                    res.append([nums[first], nums[second], nums[third]]) 
                    # move pointers
                    second += 1 
                    third -= 1
                    # duplicate check for pointers, if so then move ahead
                    while second < third and nums[second] == nums[second-1]:
                        second += 1
                    while second < third and nums[third] == nums[third+1]:
                        third -= 1
                elif target < 0: # too big, move left pointer to a higher number
                    second += 1
                else: # too small, move right pointer to a lower number
                    third -= 1
        return res
                