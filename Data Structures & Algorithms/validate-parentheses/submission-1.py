class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in brackets:
                # incoming char either has to be closing counterpart of top of stack or a different opening char altogether (since key in pairs is the closing char)
                if not stack or stack[-1] != brackets[char]:
                    return False
                # pop if it is a matching closing char
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
        