from hkdsun.tree import *


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

rl = TreeNode.tree([1, 2, 3, 4, 5, None, 6])
rr = TreeNode.tree([1, 2, 3, 4, 5, None, 6])
print Solution().isSameTree(rl, rr)
