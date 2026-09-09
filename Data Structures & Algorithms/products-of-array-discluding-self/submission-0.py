class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        # prefix = [1, 1, 2, 8] (always start with 1 since multiplication by 0 is 0 + everything to left of current element)
        # suffix = [48, 24, 6, 1] everything to right of current element
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = 1

        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]

        product = 1

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = product
            product *= nums[i]

        # return is product of every element at index i for suffix and prefix array
        return [suffix[i] * prefix[i] for i in range(len(nums))]
        