from hkdsun.tree import *


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val == p.val or root.val == q.val:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

l = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
root = TreeNode.tree(l)
print Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(3)).val
