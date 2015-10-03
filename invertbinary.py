# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        else:
            root.right, root.left = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root


n4 = TreeNode(4)
n2 = TreeNode(2)
n7 = TreeNode(7)
n3 = TreeNode(3)
n6 = TreeNode(6)
n9 = TreeNode(9)
n4.left, n4.right = n2, n7
n2.right = n3
n7.left, n7.right = n6, n9



i = Solution().invertTree(n4)
print i.val
print i.left.val
print i.left.left.val
print i.left.right.val
print i.right.val
print i.right.left.val
