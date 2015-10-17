from hkdsun.tree import *


class Solution(object):

    def is_leaf(self, node):
        if not node.left and not node.right:
            return True
        return False

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root, [], res)
        r = []
        for lis in res:
            r.append("->".join(map(lambda x: str(x.val), lis)))
        return r

    def dfs(self, root, path, res):
        if not root:
            return
        if self.is_leaf(root):
            res.append(path + [root])
            return
        self.dfs(root.left, path + [root], res)
        self.dfs(root.right, path + [root], res)

root = TreeNode.tree([1, 2, 3])
print Solution().binaryTreePaths(root)
