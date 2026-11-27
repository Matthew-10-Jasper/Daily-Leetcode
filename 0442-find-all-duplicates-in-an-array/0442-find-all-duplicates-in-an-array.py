class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen =set()
        arr=[]
        for i in nums:
            if i in seen:
                arr.append(i)
            else:
                seen.add(i)
        return arr