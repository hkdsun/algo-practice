 Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum = sum - root.val

        if not root.left and not root.right and sum == 0:
            return True

        resl, resr = False, False

        if root.left:
            resl = self.hasPathSum(root.left, sum)
        if root.right:
            resr = self.hasPathSum(root.right, sum)

        return (resr or resl)


sum = 22
print Solution().hasPathSum(n5)
