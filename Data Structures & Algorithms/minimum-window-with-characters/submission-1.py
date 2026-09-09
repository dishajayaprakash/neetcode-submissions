class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        if len(t) > len(s): return ""
        t_counter = Counter(t)
        s_counter = {}
        start = 0
        # distinct character requirements from t that are currently satisfied. we need to have at least len(t) chars in the window to have a valid window
        have, need = 0, len(t_counter)
        # res stores indices of the valid window, and res_len is current minimum window length
        res, res_len = [-1, -1], float("inf")
        for end in range(len(s)):
            c = s[end]
            # update s_counter with char entering the window 
            s_counter[c] = s_counter.get(c, 0) + 1
            # if this char is in t and the count of this char in s == count of this char in c, then increment have
            if c in t_counter and s_counter[c] == t_counter[c]:
                have += 1
            # as long as have == need, we have a possible valid window
            while have == need:
                # if curr window len is less than res_len, then update res with curr start and end indices and the res_len as well
                if (end - start + 1) < res_len:
                    res = [start, end]
                    res_len = end - start + 1
                # time to move on and shrink window to find other possible candidates
                s_counter[s[start]] -= 1
                # if the char leaving the window is present in t, then we have one less char than required for a valid window so decrement "have"
                if s[start] in t_counter and s_counter[s[start]] < t_counter[s[start]]:
                    have -= 1
                # shrink window
                start += 1
        start, end = res
        return s[start: end + 1] if res_len != float("inf") else ""


        