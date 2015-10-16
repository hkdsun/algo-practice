# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            r = []
            while queue:
                r.append(queue.pop(0))
            res.append(map(lambda c: c.val, r))
            for node in r:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
