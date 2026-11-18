# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        r = root.left
        s = root.right
        def isSameTree(p, q):
        
            if p is None and q is None:
                return True
        
            if p is None or q is None:
                return False
        
            if p.val != q.val:
                return False
        
            return (isSameTree(p.left, q.right) and
                isSameTree(p.right, q.left))
        return isSameTree(r, s)