class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        pos=[]
        for i,ch in enumerate(boxes):
            if ch=='1':
                pos.append(i)
        arr=[]
        for i in range(len(boxes)):
            c=0
            for j in pos:
                c+=abs(j-i)
            arr.append(c)
        return arr