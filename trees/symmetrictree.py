from hkdsun.tree import *


class Solution(object):
    def is_leaf(self, root):
        if not root.left and not root.right:
            return True
        return False

    def dfs(self, root):
        if not root:
            return []
        if self.is_leaf(root):
            return [root.val]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left + right + [root.val]

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left == right


print Solution().isSymmetric(TreeNode.tree([1, 2, 2, None, 4, 3, 4]))
