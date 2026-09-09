class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores indices
        for current_day in range(len(temperatures)):
            # while the stack is not empty and the current temperature is warmer than the temperature of index at top of the stack, pop and update res
            while stack and temperatures[current_day] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                res[previous_day] = current_day - previous_day
            stack.append(current_day)
        return res