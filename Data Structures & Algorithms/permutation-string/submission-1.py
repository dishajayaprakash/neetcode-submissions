class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_counter = Counter(s1)
        s2_counter = {}
        start = 0
        for end in range(len(s2)):
            s2_counter[s2[end]] = s2_counter.get(s2[end], 0) + 1
            if end - start + 1 == len(s1):
                if s1_counter == s2_counter:
                    return True
                s2_counter[s2[start]] -= 1
                if s2_counter[s2[start]] == 0:
                    del s2_counter[s2[start]]
                start += 1
        return False