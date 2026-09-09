class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # as long as the current character is part of the window and is already present in the hash set, keep removing it form the hashset and shrink the window by incrementing the left pointer
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # add char to seen set and then calculate max value for the len
            seen.add(s[r])
            res = max(res, r - l + 1)

        return res
        