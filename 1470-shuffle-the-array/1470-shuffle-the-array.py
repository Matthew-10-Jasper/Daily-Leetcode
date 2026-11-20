class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr = [0]*2*n
        c=0
        for i in range(n):
            arr[c] = nums[i]
            c+=1
            arr[c] = nums[i+n]
            c+=1
        return arr
        