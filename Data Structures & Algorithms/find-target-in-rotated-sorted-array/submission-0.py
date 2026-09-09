class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low
        # Search left half
        if nums[pivot] <= target <= nums[len(nums) - 1]:
            return self.binary_search(nums, pivot, len(nums) - 1, target)
        # Search right half
        return self.binary_search(nums, 0, pivot - 1, target)
    def binary_search(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        