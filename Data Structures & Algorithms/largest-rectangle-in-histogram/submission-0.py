class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # (index, height) pair
        for i, h in enumerate(heights):
            start = i
            # while the stack is not empty and the top height is greater than h 
            while stack and stack[-1][1] > h:
                # because we can no longer extend to the right 
                index, height = stack.pop()
                area = max(area, height * (i - index))
                # set start = index (the new bar can start from here).
                start = index
            stack.append((start, h))
        
        # process remaining bars in the stack:
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        
        return area
        