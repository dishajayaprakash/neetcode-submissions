class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            # increment the freq count of the char entering the window
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            # get the max freq of the map
            max_freq = max(freq_map.values())
            curr_len = end - start + 1
            # curr len - max number of characters you can replace must be <= given k 
            # because you can replace at most k characters in the window
            if curr_len - max_freq > k:
                # decrement the freq count of the char entering the window
                freq_map[s[start]] = freq_map.get(s[start], 0) - 1
                # shrink window
                start += 1
            max_len = max(end - start + 1, max_len)

        return max_len