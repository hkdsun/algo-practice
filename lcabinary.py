from hkdsun.tree import *


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        elif right:
            return right
        else:
            return None


l = [-1, 0, 3, -2, 4, None, None, 8]
nodes = map(lambda x: TreeNode(x) if x is not None else None, l)
root = TreeNode.tree(nodes)
print Solution().lowestCommonAncestor(root, nodes[len(l)-1], nodes[4]).val
