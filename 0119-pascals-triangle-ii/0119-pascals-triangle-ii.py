class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            for j in range(len(row)-1,0,-1):
                row[j] = row[j]+row[j-1]
            row.append(1)
        return row