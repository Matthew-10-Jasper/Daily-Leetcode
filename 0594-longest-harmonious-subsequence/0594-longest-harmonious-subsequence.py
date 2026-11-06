class Solution(object):
    def findLHS(self, nums):
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        mc = 0

        for i in freq:
            if i + 1 in freq:
                mc = max(mc, freq[i] + freq[i + 1])

        return mc