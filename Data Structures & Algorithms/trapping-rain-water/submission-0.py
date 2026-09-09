class Solution:
    def trap(self, height: List[int]) -> int:
        # basic formula is min(left_max, right_max) - height[curr_index]
        if not height: return 0
        left, right = 0, len(height) - 1
        # max value to right and left of current index because that is what controls the amount of water that can be trapped
        left_max, right_max = height[left], height[right]
        rain = 0
        while left < right:
            # per basic formula, if left_max is the min value, then move left pointer over one unit, update the value for next iteration (since we have already moved over left to one unit beyond current index) and calculate units of rainwater
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                rain += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                rain += right_max - height[right]
        return rain
        