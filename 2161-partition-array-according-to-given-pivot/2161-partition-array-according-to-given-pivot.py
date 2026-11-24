class Solution(object):
    def pivotArray(self, nums, pivot):
        less = []
        equal = []
        greater = []

        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)

        return less + equal + greater
            