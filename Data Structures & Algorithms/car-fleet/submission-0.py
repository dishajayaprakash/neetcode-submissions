class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair each car's position with its speed.
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            # append the time it takes to reach the target i.e., distance / speed
            stack.append((target - p) / s)
            # if the new car’s time is less than or equal to the time before it, it catches up and merges with that fleet → pop it from the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)        