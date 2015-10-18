from hkdsun.tree import *


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        visited = set()
        while stack:
            head = stack.pop()
            if head.left and head.left not in visited:
                stack.append(head)
                stack.append(head.left)
                visited.add(head.left)
                continue
            res.append(head.val)
            if head.right:
                stack.append(head.right)
        return res

root = TreeNode.tree([1, None, 2, 3])
print Solution().inorderTraversal(root)
