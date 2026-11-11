class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(set(nums))
        if len(arr)<3:
            return arr[-1]
        return arr[-3]
