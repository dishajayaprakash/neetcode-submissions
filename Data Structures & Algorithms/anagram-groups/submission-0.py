class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # build a "frequency signature" like (a, b, c, ..., z) where each value is count of that letter in the word
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # frequency map must be same for anagrams
            res[tuple(count)].append(s)
        return list(res.values())

        