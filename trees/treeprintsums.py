# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(root, sum, [], ans)
        return ans

    def dfs(self, root, sum, path, ans):
        if not root:
            return

        s = sum - root.val

        if self.leaf(root) and s == 0:
            ans.append(path+[root.va])
            return

        self.dfs(root.left, s, path+[root.val], ans)
        self.dfs(root.right, s, path+[root.val], ans)

    def leaf(self, node):
        if not node:
            return False
        if not node.left and not node.right:
            return True
        return False
