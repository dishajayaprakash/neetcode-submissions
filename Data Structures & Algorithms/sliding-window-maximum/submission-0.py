class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            # expand window
            heapq.heappush(heap, (-nums[i], i))
            # once the window size becomes k
            if i >= k-1:
                # remove elements from the heap if their index is outside the window
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                # top of the heap now gives the maximum for the window
                output.append(-heap[0][0])
        return output
            
        