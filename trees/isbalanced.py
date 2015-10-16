from hkdsun.tree import *


class Solution(object):

    def height(self, root, res):
        if root is None:
            return 0
        left = self.height(root.left, res)
        right = self.height(root.right, res)
        if abs(left - right) > 1:
            res[0] = False
        return 1 + max(left, right)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        res = [True]
        self.height(root, res)
        return res[0]

l = [-1, 0, 3, -2, 4, 3, None, 8]
root = TreeNode.tree(l)
print Solution().isBalanced(root)
