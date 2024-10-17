from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # should have the same length
        length = len(s)

        m1 = defaultdict(int)
        m2 = defaultdict(int)

        for i in range(length):
            m1[s[i]] += 1
            m2[t[i]] += 1

        return m1 == m2
