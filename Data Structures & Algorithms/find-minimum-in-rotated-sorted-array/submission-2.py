class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]: # we have found the pivot
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]: # you're in the left or rotated part of the array and the sorted part is actually to your right
                l = mid + 1
            else:
                r = mid - 1
        return res
        