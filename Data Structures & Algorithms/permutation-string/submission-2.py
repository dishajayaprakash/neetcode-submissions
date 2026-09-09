from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = {}
        start = 0

        for end in range(len(s2)):
            # increment count of char entering the window
            s2_counter[s2[end]] = s2_counter.get(s2[end], 0) + 1

            # window must exactly be the size of s1 
            if end - start + 1 == len(s1):

                # since permutation means all counts have to match
                if s1_counter == s2_counter:
                    return True

                # decrement count of char leaving the window
                s2_counter[s2[start]] -= 1

                # if count of char at start of window becomes zero, delete the key
                if s2_counter[s2[start]] == 0:
                    del s2_counter[s2[start]]

                # shrink window
                start += 1

        return False

        
        