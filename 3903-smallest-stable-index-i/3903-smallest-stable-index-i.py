class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            ma = max(nums[0:i+1])
            mi = min(nums[i:])
            if ma - mi <= k:
                return i
        return -1