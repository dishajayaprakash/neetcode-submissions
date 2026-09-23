#Think of placing the two arrays side by side and making a cut (partition) so that:
# The left side of the cut contains exactly half of the total elements (or half + 1 if odd).
# All elements on the left side are <= all elements on the right side.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l+r) // 2 # a 
            j = half - i - 2 # calculate the left partition size of the longer array, -2 because the arrays are 0 indexed
            # for the shorter array, the left partition is just 0 to mid
            a_left = a[i] if i >= 0 else float("-inf") # to prevent out of bounds errors
            a_right = a[i+1] if (i+1) < len(a) else float("inf")
            b_left = b[j] if j >= 0 else float("-inf")
            b_right = b[j+1] if (j+1) < len(b) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right: # basically saying that we have too many elements from A, so reduce it by update right pointer
                r = i-1
            else:
                l = i+1


