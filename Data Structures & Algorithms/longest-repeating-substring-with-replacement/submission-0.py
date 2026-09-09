class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            curr_len = end - start + 1
            curr_max_freq = max(freq_map.values())
            if curr_len - curr_max_freq > k:
                freq_map[s[start]] = freq_map.get(s[start], 0) - 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
            
        