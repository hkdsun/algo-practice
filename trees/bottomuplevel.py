from hkdsun.tree import *


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, res, 0)
        return res

    def dfs(self, root, res, level):
        if not root:
            return
        if len(res) < level + 1:
            res.insert(0, [])
        print res, level
        res[-(level+1)].append(root.val)
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        stack = [root]
        res = []
        while stack:
            cur_level = []
            while stack:
                cur_level.append(stack.pop(0))
            res.append([x.val for x in cur_level])
            for node in cur_level:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res

l = [3, 9, 20, 8, 10, 15, 7]
root = TreeNode.tree(l)
print Solution().levelOrderBottom(root)
